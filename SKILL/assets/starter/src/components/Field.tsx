import { useId } from 'react';
import type { InputHTMLAttributes, ReactNode, TextareaHTMLAttributes } from 'react';
import { cn } from '../lib/cn';

interface ShellProps {
  label: string;
  hint?: string;
  error?: string;
  optional?: boolean;
  children: (a11y: { id: string; describedBy: string | undefined; invalid: boolean }) => ReactNode;
}

/** Label + control + hint + error, wired with htmlFor / aria-describedby / aria-invalid. */
function FieldShell({ label, hint, error, optional, children }: ShellProps) {
  const id = useId();
  const hintId = `${id}-hint`;
  const errId = `${id}-err`;
  const describedBy = [hint && hintId, error && errId].filter(Boolean).join(' ') || undefined;
  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={id} className="text-sm font-medium text-fg">
        {label}
        {optional && <span className="ms-1 font-normal text-muted">(optional)</span>}
      </label>
      {children({ id, describedBy, invalid: Boolean(error) })}
      {hint && !error && (
        <p id={hintId} className="text-sm text-muted">
          {hint}
        </p>
      )}
      {error && (
        <p id={errId} className="flex items-start gap-1.5 text-sm text-danger">
          <svg className="mt-0.5 size-4 shrink-0" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path d="M10 2 1 18h18L10 2Zm1 12H9v-2h2v2Zm0-4H9V7h2v3Z" />
          </svg>
          <span>{error}</span>
        </p>
      )}
    </div>
  );
}

const control =
  'w-full min-h-11 rounded-ui ui-border border-line-strong bg-surface px-3 py-2 text-fg ' +
  'placeholder:text-muted transition-colors ' +
  'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent ' +
  'aria-invalid:border-danger disabled:opacity-60 disabled:cursor-not-allowed';

type FieldMeta = Pick<ShellProps, 'label' | 'hint' | 'error' | 'optional'>;

export function TextField({ label, hint, error, optional, className, ...rest }: FieldMeta & Omit<InputHTMLAttributes<HTMLInputElement>, 'id'>) {
  return (
    <FieldShell label={label} hint={hint} error={error} optional={optional}>
      {({ id, describedBy, invalid }) => (
        <input id={id} aria-describedby={describedBy} aria-invalid={invalid || undefined} className={cn(control, className)} {...rest} />
      )}
    </FieldShell>
  );
}

export function TextAreaField({ label, hint, error, optional, className, ...rest }: FieldMeta & Omit<TextareaHTMLAttributes<HTMLTextAreaElement>, 'id'>) {
  return (
    <FieldShell label={label} hint={hint} error={error} optional={optional}>
      {({ id, describedBy, invalid }) => (
        <textarea id={id} aria-describedby={describedBy} aria-invalid={invalid || undefined} className={cn(control, 'field-sizing-content min-h-24', className)} {...rest} />
      )}
    </FieldShell>
  );
}
