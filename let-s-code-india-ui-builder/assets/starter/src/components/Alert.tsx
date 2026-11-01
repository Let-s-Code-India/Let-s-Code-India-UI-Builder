import type { ReactNode } from 'react';
import { cn } from '../lib/cn';

type Tone = 'info' | 'success' | 'warning' | 'danger';

const tones: Record<Tone, { stripe: string; text: string; glyph: string }> = {
  info: { stripe: 'border-s-info', text: 'text-info', glyph: 'i' },
  success: { stripe: 'border-s-success', text: 'text-success', glyph: '✓' },
  warning: { stripe: 'border-s-warning', text: 'text-warning', glyph: '▲' },
  danger: { stripe: 'border-s-danger', text: 'text-danger', glyph: '✕' },
};

/** Danger alerts interrupt screen readers (role="alert"); others are polite (role="status"). */
export function Alert({ tone = 'info', title, children }: { tone?: Tone; title: string; children?: ReactNode }) {
  const t = tones[tone];
  return (
    <div
      role={tone === 'danger' ? 'alert' : 'status'}
      className={cn('flex gap-3 rounded-ui ui-border border-s-4 border-line bg-surface p-4', t.stripe)}
    >
      <span aria-hidden="true" className={cn('mt-0.5 font-bold', t.text)}>
        {t.glyph}
      </span>
      <div className="flex flex-col gap-1">
        <p className={cn('font-semibold', t.text)}>{title}</p>
        {children && <div className="text-sm text-fg">{children}</div>}
      </div>
    </div>
  );
}
