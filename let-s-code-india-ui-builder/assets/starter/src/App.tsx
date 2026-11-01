import { useState } from 'react';
import type { CSSProperties, FormEvent } from 'react';
import { Alert } from './components/Alert';
import { Badge } from './components/Badge';
import { Button } from './components/Button';
import { Card } from './components/Card';
import { Dialog, DialogTrigger } from './components/Dialog';
import { EmptyState } from './components/EmptyState';
import { TextAreaField, TextField } from './components/Field';
import { Skeleton } from './components/Skeleton';
import { ThemeToggle } from './components/ThemeToggle';

/*
 * DESIGN PLAN (replace for your project)
 *   Subject    : developer-facing UI starter. Audience: people shipping a first product page. Job: copy, adapt, ship.
 *   Direction  : clean product UI, one calm accent, strong states.
 *   Palette    : 30 clean-minimalist-saas (system theme)      Type: DM Sans (+ Devanagari fallback)
 *   Surface    : soft (switchable: glass | brutal | terminal | editorial | organic)
 *   Signature  : every state is designed - focus, loading, error, empty, destructive confirmation.
 */

const styles = ['soft', 'glass', 'brutal', 'terminal', 'editorial', 'organic'] as const;

function StyleSwitcher() {
  return (
    <label className="flex items-center gap-2 text-sm font-medium">
      Style
      <select
        defaultValue="soft"
        onChange={(e) => {
          document.documentElement.dataset.style = e.target.value;
        }}
        className="min-h-11 rounded-ui ui-border border-line-strong bg-surface px-3 text-fg"
      >
        {styles.map((s) => (
          <option key={s} value={s}>
            {s}
          </option>
        ))}
      </select>
    </label>
  );
}

export default function App() {
  const [sending, setSending] = useState(false);
  const [sent, setSent] = useState(false);
  const [email, setEmail] = useState('');
  const [loadingList, setLoadingList] = useState(false);
  const [deleted, setDeleted] = useState<string>('');

  const emailError = email.length > 0 && !email.includes('@') ? 'Enter an email address like name@example.com.' : undefined;

  function submit(e: FormEvent) {
    e.preventDefault();
    if (emailError) return;
    setSending(true);
    setSent(false);
    window.setTimeout(() => {
      setSending(false);
      setSent(true);
    }, 1200);
  }

  return (
    <>
      <a
        href="#main"
        className="absolute left-4 top-4 z-50 -translate-y-24 rounded-ui bg-accent px-4 py-2 font-medium text-accent-fg focus-visible:translate-y-0"
      >
        Skip to main content
      </a>

      <header className="sticky top-0 z-40 border-b border-line bg-canvas/90 backdrop-blur-sm">
        <div className="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-3 px-4 py-3 sm:px-6">
          <p className="font-display text-lg font-bold">Let-s-Code-India UI Starter</p>
          <div className="flex flex-wrap items-center gap-3">
            <StyleSwitcher />
            <ThemeToggle />
          </div>
        </div>
      </header>

      <main id="main" className="mx-auto flex max-w-5xl flex-col gap-16 px-4 py-12 sm:px-6 sm:py-16">
        <section aria-labelledby="hero-title" className="rise flex flex-col gap-5" style={{ '--i': 1 } as CSSProperties}>
          <h1 id="hero-title" className="max-w-3xl text-[clamp(2.25rem,1.2rem+4.5vw,4.5rem)] font-bold tracking-tight">
            Every colour pair here already passes contrast.
          </h1>
          <p className="max-w-prose text-lg text-muted">
            Pick a palette, generate the tokens, then build with components that already handle focus, loading, error
            and empty states. Change the style or theme above and nothing needs rewriting.
          </p>
          <a href="#contact" className="w-fit font-medium text-accent underline underline-offset-4">
            Jump to the form example
          </a>
        </section>

        <section aria-labelledby="status-title" className="flex flex-col gap-4">
          <h2 id="status-title" className="text-2xl font-semibold">
            Status never relies on colour alone
          </h2>
          <div className="flex flex-wrap gap-2">
            <Badge tone="success">Deployed</Badge>
            <Badge tone="warning">Needs review</Badge>
            <Badge tone="danger">Build failed</Badge>
            <Badge tone="info">Draft</Badge>
            <Badge tone="accent">New</Badge>
          </div>
          <Alert tone="warning" title="Two fields need attention">
            Each badge and alert pairs its colour with a symbol and a text label.
          </Alert>
        </section>

        <section id="contact" aria-labelledby="form-title" className="grid gap-8 md:grid-cols-2">
          <div className="flex flex-col gap-3">
            <h2 id="form-title" className="text-2xl font-semibold">
              Forms that explain themselves
            </h2>
            <p className="text-muted">
              Labels are real labels, errors say what to fix, and the button shows progress without losing its label.
            </p>
          </div>
          <Card as="section" aria-label="Contact form">
            <form onSubmit={submit} noValidate className="flex flex-col gap-4">
              <TextField label="Your name" name="name" autoComplete="name" required />
              <TextField
                label="Email"
                name="email"
                type="email"
                autoComplete="email"
                inputMode="email"
                hint="We only use this to reply."
                error={emailError}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <TextAreaField label="Message" name="message" optional placeholder="What are you building?" />
              <Button type="submit" loading={sending}>
                {sending ? 'Sending…' : 'Send message'}
              </Button>
              {sent && (
                <Alert tone="success" title="Message sent">
                  Thanks. We will reply within two working days.
                </Alert>
              )}
            </form>
          </Card>
        </section>

        <section aria-labelledby="dialog-title" className="flex flex-col gap-4">
          <h2 id="dialog-title" className="text-2xl font-semibold">
            Destructive actions ask first
          </h2>
          <div className="flex flex-wrap items-center gap-4">
            <DialogTrigger dialogId="delete-project" variant="danger">
              Delete project
            </DialogTrigger>
            <p aria-live="polite" className="text-muted">
              {deleted === 'delete' ? 'Project deleted.' : deleted === 'cancel' ? 'Nothing was deleted.' : ''}
            </p>
          </div>
          <Dialog
            id="delete-project"
            title="Delete this project?"
            onClose={(v) => setDeleted(v)}
            actions={
              <>
                <Button variant="secondary" type="submit" value="cancel">
                  Keep project
                </Button>
                <Button variant="danger" type="submit" value="delete">
                  Delete project
                </Button>
              </>
            }
          >
            This removes the project and its 14 builds. You cannot undo this.
          </Dialog>
        </section>

        <section aria-labelledby="states-title" className="flex flex-col gap-4">
          <h2 id="states-title" className="text-2xl font-semibold">
            Loading and empty states
          </h2>
          <div>
            <Button variant="secondary" onClick={() => setLoadingList((v) => !v)}>
              {loadingList ? 'Show empty state' : 'Show loading state'}
            </Button>
          </div>
          {loadingList ? (
            <div role="status" aria-label="Loading projects" className="flex flex-col gap-3">
              <Skeleton className="h-16" />
              <Skeleton className="h-16" />
              <Skeleton className="h-16" />
            </div>
          ) : (
            <EmptyState title="No projects yet" action={<Button size="sm">Create your first project</Button>}>
              Projects you create appear here, with their latest build status.
            </EmptyState>
          )}
        </section>
      </main>

      <footer className="border-t border-line py-8 text-center text-sm text-muted">
        Built with Let-s-Code-India-UI-Builder
      </footer>
    </>
  );
}
