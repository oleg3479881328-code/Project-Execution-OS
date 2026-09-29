import { createHash } from 'node:crypto'

import type { SiteInstanceV01 } from '@/site-model/types'
import { carServiceGarage } from '@/sites/car-service-garage'

export const CSG_STATE_PATH = 'projects/website-creation/engine/src/sites/car-service-garage-state.json'
export const CSG_MEDIA_PATH = 'projects/website-creation/engine/public/uploads/csg'

type GitRef = { object?: { sha?: string } }
type GitCommit = { tree?: { sha?: string } }
type GitBlob = { sha?: string }
type GitTree = { sha?: string }
type GitCommitResult = { sha?: string; html_url?: string }
type GitFile = { content?: string; encoding?: string; sha?: string }

type FileWrite = {
  path: string
  content: string
  encoding: 'utf-8' | 'base64'
}

export class CsgGitError extends Error {
  constructor(message: string, readonly status: number) {
    super(message)
    this.name = 'CsgGitError'
  }
}

function config() {
  return {
    repo: process.env.CSG_GITHUB_REPO?.trim() || 'oleg3479881328-code/Project-Execution-OS',
    stagingBranch: process.env.CSG_GITHUB_STAGING_BRANCH?.trim() || 'csg-content-staging',
    productionBranch: process.env.CSG_GITHUB_PRODUCTION_BRANCH?.trim() || 'main',
    statePath: process.env.CSG_GITHUB_STATE_PATH?.trim() || CSG_STATE_PATH,
    apiBase: (process.env.CSG_GITHUB_API_BASE_URL?.trim() || 'https://api.github.com').replace(/\/$/, ''),
  }
}

function token() {
  return process.env.CSG_GITHUB_TOKEN?.trim() || ''
}

export function isCsgGitConfigured() {
  return Boolean(token())
}

function githubPath(path: string) {
  return path.split('/').map(encodeURIComponent).join('/')
}

async function githubRequest<T>(path: string, init: RequestInit = {}): Promise<T> {
  const auth = token()
  if (!auth) throw new CsgGitError('CSG_GITHUB_TOKEN is not configured.', 503)

  const response = await fetch(`${config().apiBase}${path}`, {
    ...init,
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${auth}`,
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
      ...(init.headers || {}),
    },
    cache: 'no-store',
  })
  const raw = await response.text()
  let body: unknown = {}
  try {
    body = raw ? JSON.parse(raw) : {}
  } catch {
    body = {}
  }
  if (!response.ok) {
    const message = body && typeof body === 'object' && 'message' in body
      ? String((body as { message?: unknown }).message)
      : `GitHub request failed with ${response.status}`
    throw new CsgGitError(message, response.status)
  }
  return body as T
}

async function getRef(branch: string) {
  const { repo } = config()
  return githubRequest<GitRef>(`/repos/${repo}/git/ref/heads/${encodeURIComponent(branch)}`)
}

async function ensureStagingBranch() {
  const { repo, productionBranch, stagingBranch } = config()
  try {
    const ref = await getRef(stagingBranch)
    if (!ref.object?.sha) throw new CsgGitError('Staging branch has no head commit.', 502)
    return ref.object.sha
  } catch (error) {
    if (!(error instanceof CsgGitError) || error.status !== 404) throw error
    const productionRef = await getRef(productionBranch)
    const sha = productionRef.object?.sha
    if (!sha) throw new CsgGitError('Production branch has no head commit.', 502)
    const created = await githubRequest<GitRef>(`/repos/${repo}/git/refs`, {
      method: 'POST',
      body: JSON.stringify({ ref: `refs/heads/${stagingBranch}`, sha }),
    })
    if (!created.object?.sha) throw new CsgGitError('Could not create the CSG staging branch.', 502)
    return created.object.sha
  }
}

async function readFile(path: string, branch: string): Promise<GitFile | null> {
  const { repo } = config()
  try {
    return await githubRequest<GitFile>(`/repos/${repo}/contents/${githubPath(path)}?ref=${encodeURIComponent(branch)}`)
  } catch (error) {
    if (error instanceof CsgGitError && error.status === 404) return null
    throw error
  }
}

function decodeFile(file: GitFile) {
  if (!file.content) return null
  return Buffer.from(file.content.replace(/\s/g, ''), file.encoding === 'base64' ? 'base64' : 'utf8').toString('utf8')
}

function serializeState(state: SiteInstanceV01) {
  return `${JSON.stringify(state, null, 2)}\n`
}

export function validateCsgState(value: unknown): value is SiteInstanceV01 {
  if (!value || typeof value !== 'object') return false
  const state = value as Partial<SiteInstanceV01>
  const page = state.pages?.[0]
  return state.schemaVersion === '0.1-draft'
    && state.siteId === 'car-service-garage-ohio'
    && Boolean(state.business?.contact?.phone)
    && Boolean(page?.isHomepage)
    && Boolean(page?.puckData && Array.isArray(page.puckData.content))
}

export async function readCsgState(branch: string): Promise<SiteInstanceV01> {
  if (!isCsgGitConfigured()) return carServiceGarage
  const file = await readFile(config().statePath, branch)
  if (!file) return carServiceGarage
  const parsed = JSON.parse(decodeFile(file) || '{}') as unknown
  if (!validateCsgState(parsed)) throw new CsgGitError('The CSG canonical state failed validation.', 422)
  return parsed
}

export async function loadEditorState() {
  if (!isCsgGitConfigured()) return { state: carServiceGarage, durable: false as const }
  await ensureStagingBranch()
  return { state: await readCsgState(config().stagingBranch), durable: true as const }
}

async function commitFiles(branch: string, files: FileWrite[], message: string) {
  const { repo } = config()
  const headSha = branch === config().stagingBranch ? await ensureStagingBranch() : (await getRef(branch)).object?.sha
  if (!headSha) throw new CsgGitError(`Branch ${branch} has no head commit.`, 502)
  const headCommit = await githubRequest<GitCommit>(`/repos/${repo}/git/commits/${headSha}`)
  const baseTree = headCommit.tree?.sha
  if (!baseTree) throw new CsgGitError(`Branch ${branch} has no tree.`, 502)

  const entries = await Promise.all(files.map(async (file) => {
    const blob = await githubRequest<GitBlob>(`/repos/${repo}/git/blobs`, {
      method: 'POST',
      body: JSON.stringify({ content: file.content, encoding: file.encoding }),
    })
    if (!blob.sha) throw new CsgGitError(`Could not create repository blob for ${file.path}.`, 502)
    return { path: file.path, mode: '100644', type: 'blob', sha: blob.sha }
  }))

  const tree = await githubRequest<GitTree>(`/repos/${repo}/git/trees`, {
    method: 'POST',
    body: JSON.stringify({ base_tree: baseTree, tree: entries }),
  })
  if (!tree.sha) throw new CsgGitError('Could not create the CSG content tree.', 502)

  const commit = await githubRequest<GitCommitResult>(`/repos/${repo}/git/commits`, {
    method: 'POST',
    body: JSON.stringify({ message, tree: tree.sha, parents: [headSha] }),
  })
  if (!commit.sha) throw new CsgGitError('Could not create the CSG content commit.', 502)

  await githubRequest(`/repos/${repo}/git/refs/heads/${encodeURIComponent(branch)}`, {
    method: 'PATCH',
    body: JSON.stringify({ sha: commit.sha, force: false }),
  })
  return { ...commit, branch }
}

export async function saveCsgDraft(state: SiteInstanceV01) {
  if (!validateCsgState(state)) throw new CsgGitError('The CSG draft failed validation.', 422)
  if (!isCsgGitConfigured()) throw new CsgGitError('CSG_GITHUB_TOKEN is not configured.', 503)
  const { stagingBranch, statePath } = config()
  return commitFiles(stagingBranch, [{ path: statePath, content: serializeState(state), encoding: 'utf-8' }], 'CSG editor: save draft')
}

function safeSegment(value: string) {
  return value.toLowerCase().replace(/[^a-z0-9-]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80) || 'image'
}

function extensionFor(type: string, name: string) {
  const original = name.match(/\.[a-z0-9]+$/i)?.[0]?.toLowerCase()
  if (original && ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'].includes(original)) return original
  return ({ 'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp', 'image/gif': '.gif', 'image/avif': '.avif' } as Record<string, string>)[type] || '.bin'
}

export async function uploadCsgMedia(file: File, alt: string) {
  if (!isCsgGitConfigured()) throw new CsgGitError('CSG_GITHUB_TOKEN is not configured.', 503)
  if (!file.type.startsWith('image/')) throw new CsgGitError('Only image uploads are allowed.', 415)
  if (file.size > 8 * 1024 * 1024) throw new CsgGitError('Image uploads must be 8 MB or smaller.', 413)
  const bytes = Buffer.from(await file.arrayBuffer())
  const isPng = bytes.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))
  const isJpeg = bytes.subarray(0, 2).equals(Buffer.from([255, 216]))
  const isGif = bytes.subarray(0, 6).toString('ascii') === 'GIF87a' || bytes.subarray(0, 6).toString('ascii') === 'GIF89a'
  const isWebp = bytes.subarray(0, 4).toString('ascii') === 'RIFF' && bytes.subarray(8, 12).toString('ascii') === 'WEBP'
  const isAvif = bytes.subarray(4, 12).toString('ascii').includes('ftyp')
  if (!(isPng || isJpeg || isGif || isWebp || isAvif)) throw new CsgGitError('The uploaded file is not a recognized image.', 415)
  const digest = createHash('sha256').update(bytes).digest('hex')
  const filename = `${digest.slice(0, 20)}-${safeSegment(file.name.replace(/\.[^.]+$/, ''))}${extensionFor(file.type, file.name)}`
  const path = `${CSG_MEDIA_PATH}/${filename}`
  const result = await commitFiles(config().stagingBranch, [{ path, content: bytes.toString('base64'), encoding: 'base64' }], `CSG editor: upload ${filename}`)
  return {
    id: `csg-${digest}`,
    url: `/uploads/csg/${filename}`,
    alt: alt.trim() || file.name.replace(/\.[^.]+$/, '').replace(/[-_]+/g, ' '),
    mimeType: file.type,
    filename,
    commitSha: result.sha,
  }
}

export function approvedCsgMedia() {
  return ['hero', 'diagnostics', 'brakes', 'suspension', 'oil', 'electrical', 'major'].map((name) => ({
    id: `seed-csg-${name}`,
    url: `/assets/${name}.webp`,
    alt: `Car Service Garage ${name} service photograph`,
    filename: `${name}.webp`,
    mimeType: 'image/webp',
  }))
}

export async function publishCsgDraft() {
  if (!isCsgGitConfigured()) throw new CsgGitError('CSG_GITHUB_TOKEN is not configured.', 503)
  const { repo, stagingBranch, productionBranch } = config()
  const draft = await readCsgState(stagingBranch)
  if (!validateCsgState(draft)) throw new CsgGitError('The CSG staging state failed validation.', 422)
  const stagingSha = (await getRef(stagingBranch)).object?.sha
  if (!stagingSha) throw new CsgGitError('The CSG staging branch has no head commit.', 502)
  const mergeResponse = await fetch(`${config().apiBase}/repos/${repo}/merges`, {
    method: 'POST',
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${token()}`,
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ base: productionBranch, head: stagingBranch, commit_message: 'CSG editor: publish to production' }),
    cache: 'no-store',
  })
  const raw = await mergeResponse.text()
  if (!mergeResponse.ok && mergeResponse.status !== 204) {
    let message = `GitHub merge failed with ${mergeResponse.status}`
    try { message = String((JSON.parse(raw) as { message?: string }).message || message) } catch { /* keep safe generic message */ }
    throw new CsgGitError(message, mergeResponse.status)
  }
  const productionSha = (await getRef(productionBranch)).object?.sha
  return { commitSha: productionSha || stagingSha, stagingSha, branch: productionBranch, merged: mergeResponse.status === 201 }
}

export function csgGitConfigSummary() {
  const { repo, stagingBranch, productionBranch, statePath } = config()
  return { repo, stagingBranch, productionBranch, statePath, configured: isCsgGitConfigured() }
}
