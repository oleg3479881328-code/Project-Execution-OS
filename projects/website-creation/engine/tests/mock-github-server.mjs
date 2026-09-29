import { createHash } from 'node:crypto'
import { readFileSync } from 'node:fs'
import { createServer } from 'node:http'

const port = Number(process.env.MOCK_GITHUB_PORT || 4010)
const statePath = 'projects/website-creation/engine/src/sites/car-service-garage-state.json'
const initialState = readFileSync(new URL('../src/sites/car-service-garage-state.json', import.meta.url), 'utf8')

const refs = new Map([['main', 'main-head']])
const commits = new Map([['main-head', 'main-tree']])
const trees = new Map([['main-tree', new Map([[statePath, initialState]])]])
const blobs = new Map()
let sequence = 0

function json(response, status, body) {
  response.writeHead(status, { 'content-type': 'application/json' })
  response.end(JSON.stringify(body))
}

function cloneTree(tree) {
  return new Map(trees.get(tree) || [])
}

function newId(prefix) {
  sequence += 1
  return `${prefix}-${sequence}`
}

function branchFromRef(pathname) {
  return decodeURIComponent(pathname.split('/').pop() || '')
}

const server = createServer(async (request, response) => {
  const url = new URL(request.url || '/', `http://${request.headers.host}`)
  if (request.method === 'GET' && url.pathname === '/health') return json(response, 200, { ok: true })
  if (!url.pathname.startsWith('/repos/')) return json(response, 404, { message: 'Not found' })

  const bodyText = async () => {
    const chunks = []
    for await (const chunk of request) chunks.push(chunk)
    return chunks.length ? JSON.parse(Buffer.concat(chunks).toString('utf8')) : {}
  }
  const path = url.pathname

  if (request.method === 'GET' && path.includes('/git/ref/heads/')) {
    const branch = branchFromRef(path)
    const sha = refs.get(branch)
    return sha ? json(response, 200, { object: { sha } }) : json(response, 404, { message: 'Reference not found' })
  }
  if (request.method === 'POST' && path.endsWith('/git/refs')) {
    const input = await bodyText()
    const branch = String(input.ref || '').replace(/^refs\/heads\//, '')
    const sha = String(input.sha || '')
    if (!commits.has(sha)) return json(response, 422, { message: 'Unknown commit' })
    refs.set(branch, sha)
    return json(response, 201, { ref: `refs/heads/${branch}`, object: { sha } })
  }
  if (request.method === 'GET' && path.includes('/git/commits/')) {
    const sha = decodeURIComponent(path.split('/').pop() || '')
    const tree = commits.get(sha)
    return tree ? json(response, 200, { tree: { sha: tree } }) : json(response, 404, { message: 'Commit not found' })
  }
  if (request.method === 'POST' && path.endsWith('/git/blobs')) {
    const input = await bodyText()
    const value = String(input.content || '')
    const bytes = input.encoding === 'base64' ? Buffer.from(value, 'base64') : Buffer.from(value, 'utf8')
    const sha = createHash('sha1').update(bytes).digest('hex')
    blobs.set(sha, bytes)
    return json(response, 201, { sha })
  }
  if (request.method === 'POST' && path.endsWith('/git/trees')) {
    const input = await bodyText()
    const tree = cloneTree(String(input.base_tree || ''))
    for (const entry of input.tree || []) {
      const bytes = blobs.get(String(entry.sha))
      if (bytes) tree.set(String(entry.path), bytes.toString('utf8'))
    }
    const sha = newId('tree')
    trees.set(sha, tree)
    return json(response, 201, { sha })
  }
  if (request.method === 'POST' && path.endsWith('/git/commits')) {
    const input = await bodyText()
    const sha = newId('commit')
    commits.set(sha, String(input.tree))
    return json(response, 201, { sha, html_url: `https://github.test/commit/${sha}` })
  }
  if (request.method === 'PATCH' && path.includes('/git/refs/heads/')) {
    const branch = branchFromRef(path)
    const input = await bodyText()
    refs.set(branch, String(input.sha))
    return json(response, 200, { ref: `refs/heads/${branch}`, object: { sha: String(input.sha) } })
  }
  if (request.method === 'GET' && path.includes('/contents/')) {
    const branch = url.searchParams.get('ref') || 'main'
    const sha = refs.get(branch)
    const tree = sha ? commits.get(sha) : null
    const files = tree ? trees.get(tree) : null
    const filePath = decodeURIComponent(path.split('/contents/')[1] || '')
    const content = files?.get(filePath)
    return content === undefined
      ? json(response, 404, { message: 'File not found' })
      : json(response, 200, { path: filePath, encoding: 'base64', content: Buffer.from(content).toString('base64') })
  }
  if (request.method === 'POST' && path.endsWith('/merges')) {
    const input = await bodyText()
    const head = refs.get(String(input.head))
    if (!head) return json(response, 404, { message: 'Head branch not found' })
    const base = refs.get(String(input.base))
    if (head === base) return response.writeHead(204).end()
    refs.set(String(input.base), head)
    return json(response, 201, { sha: head, commit: { sha: head } })
  }

  return json(response, 404, { message: 'Unsupported mock GitHub request' })
})

server.listen(port, '127.0.0.1', () => console.log(`mock-github listening on ${port}`))
