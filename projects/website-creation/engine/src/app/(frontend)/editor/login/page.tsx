'use client'

import { FormEvent, useState } from 'react'

export default function CsgEditorLoginPage() {
  const [username, setUsername] = useState('editor')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setBusy(true)
    setError('')
    try {
      const response = await fetch('/api/csg/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      })
      const result = await response.json() as { error?: string }
      if (!response.ok) throw new Error(result.error || 'Login failed.')
      const next = new URLSearchParams(window.location.search).get('next') || '/editor'
      window.location.assign(next)
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : 'Login failed.')
      setBusy(false)
    }
  }

  return (
    <main className="csg-login-page">
      <form className="csg-login-card" onSubmit={submit}>
        <p className="wc-eyebrow">Car Service Garage</p>
        <h1>Open the visual editor</h1>
        <p>Changes are saved to the GitHub-backed staging branch before publishing.</p>
        <label>Username<input value={username} onChange={(event) => setUsername(event.target.value)} autoComplete="username" /></label>
        <label>Password<input value={password} onChange={(event) => setPassword(event.target.value)} type="password" autoComplete="current-password" /></label>
        {error ? <p role="alert">{error}</p> : null}
        <button type="submit" disabled={busy}>{busy ? 'Opening…' : 'Open editor'}</button>
      </form>
    </main>
  )
}
