import { useRef, useState } from 'react';
import {
  createWorkspaceBackup,
  restoreWorkspaceBackup,
  validateWorkspaceBackup,
  workspaceBackupCounts
} from '../../src/core/backup';

interface BackupControlsProps {
  extensionVersion: string;
}

export default function BackupControls({ extensionVersion }: BackupControlsProps) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState(
    'Backup includes local conversations, hydrated messages, favorites, notes, settings and health history.'
  );

  async function exportBackup() {
    setBusy(true);
    try {
      const backup = await createWorkspaceBackup(extensionVersion);
      const counts = workspaceBackupCounts(backup);
      downloadJson(backup, `chatgpt-workspace-backup-${safeTimestamp()}.json`);
      setMessage(
        `Backup exported: ${counts.conversations} conversations, ${counts.messages} messages, ${counts.ownerMetadata} owner records.`
      );
    } catch (cause) {
      setMessage(`Backup failed: ${readableError(cause)}`);
    } finally {
      setBusy(false);
    }
  }

  async function restoreFromFile(file: File) {
    setBusy(true);
    try {
      const text = await file.text();
      let parsed: unknown;
      try {
        parsed = JSON.parse(text);
      } catch {
        throw new Error('BACKUP_INVALID_JSON: Selected file is not valid JSON.');
      }

      const backup = validateWorkspaceBackup(parsed);
      const counts = workspaceBackupCounts(backup);
      const confirmed = window.confirm(
        `Restore Workspace backup from ${backup.exportedAt}?\n\n` +
          `${counts.conversations} conversations\n` +
          `${counts.messages} cached messages\n` +
          `${counts.ownerMetadata} owner metadata records\n\n` +
          'This replaces the current local Workspace database. A safety backup of the current database will download first.'
      );
      if (!confirmed) {
        setMessage('Restore cancelled. Current Workspace was not changed.');
        return;
      }

      const safetyBackup = await createWorkspaceBackup(extensionVersion);
      downloadJson(safetyBackup, `chatgpt-workspace-pre-restore-${safeTimestamp()}.json`);

      const restored = await restoreWorkspaceBackup(backup);
      setMessage(
        `Restore complete: ${restored.conversations} conversations, ${restored.messages} messages, ${restored.ownerMetadata} owner records. Reloading…`
      );
      window.setTimeout(() => window.location.reload(), 450);
    } catch (cause) {
      setMessage(`Restore failed — current Workspace preserved: ${readableError(cause)}`);
    } finally {
      if (inputRef.current) inputRef.current.value = '';
      setBusy(false);
    }
  }

  return (
    <div className="backup-controls">
      <div className="health-actions">
        <button disabled={busy} onClick={() => void exportBackup()}>
          {busy ? 'Working…' : 'Backup workspace'}
        </button>
        <button disabled={busy} onClick={() => inputRef.current?.click()}>
          Restore backup
        </button>
        <input
          ref={inputRef}
          type="file"
          accept="application/json,.json"
          hidden
          onChange={(event) => {
            const file = event.target.files?.[0];
            if (file) void restoreFromFile(file);
          }}
        />
      </div>
      <div className="diagnostic-footnote">
        {message} Backup JSON may contain private conversation content; keep it private.
      </div>
    </div>
  );
}

function downloadJson(value: unknown, filename: string): void {
  const blob = new Blob([JSON.stringify(value, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  window.setTimeout(() => URL.revokeObjectURL(url), 1_000);
}

function safeTimestamp(): string {
  return new Date().toISOString().replace(/[:.]/g, '-');
}

function readableError(cause: unknown): string {
  return cause instanceof Error ? cause.message.slice(0, 260) : String(cause).slice(0, 260);
}
