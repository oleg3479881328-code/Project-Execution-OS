import { createHmac, timingSafeEqual } from 'node:crypto'

export const CSG_EDITOR_COOKIE = 'csg_editor_session'
const SESSION_TTL_SECONDS = 60 * 60 * 24 * 30

function username() {
  return process.env.CSG_EDITOR_USERNAME?.trim() || 'editor'
}

function password() {
  return process.env.CSG_EDITOR_PASSWORD?.trim() || ''
}

function sessionSecret() {
  return process.env.CSG_EDITOR_SESSION_SECRET?.trim() || ''
}

export function isEditorAuthConfigured() {
  return Boolean(password() && sessionSecret())
}

function safeEqual(left: string, right: string) {
  const a = Buffer.from(left)
  const b = Buffer.from(right)
  return a.length === b.length && timingSafeEqual(a, b)
}

function signature(payload: string) {
  return createHmac('sha256', sessionSecret()).update(payload).digest('base64url')
}

export function verifyEditorCredentials(inputUser: string, inputPassword: string) {
  return isEditorAuthConfigured() && safeEqual(inputUser.trim(), username()) && safeEqual(inputPassword, password())
}

export function createEditorSession() {
  const expiresAt = Math.floor(Date.now() / 1000) + SESSION_TTL_SECONDS
  const payload = `${username()}.${expiresAt}`
  return `${payload}.${signature(payload)}`
}

export function verifyEditorSession(value?: string | null) {
  if (!value || !sessionSecret()) return false
  const [sessionUser, expiresRaw, actualSignature] = value.split('.')
  const expiresAt = Number(expiresRaw)
  if (!sessionUser || !actualSignature || !Number.isFinite(expiresAt) || expiresAt < Math.floor(Date.now() / 1000)) return false
  return safeEqual(sessionUser, username()) && safeEqual(actualSignature, signature(`${sessionUser}.${expiresAt}`))
}

export function editorUsername() {
  return username()
}
