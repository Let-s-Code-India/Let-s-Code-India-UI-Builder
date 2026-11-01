import type { ReactNode } from 'react';
import { cn } from '../lib/cn';

type Tone = 'neutral' | 'accent' | 'success' | 'warning' | 'danger' | 'info';

// Colour is never the only signal: every tone carries a glyph and a text label.
const tones: Record<Tone, { cls: string; glyph: string }> = {
  neutral: { cls: 'bg-fg/10 text-fg', glyph: '•' },
  accent: { cls: 'bg-accent/10 text-accent', glyph: '★' },
  success: { cls: 'bg-success/10 text-success', glyph: '✓' },
  warning: { cls: 'bg-warning/10 text-warning', glyph: '▲' },
  danger: { cls: 'bg-danger/10 text-danger', glyph: '✕' },
  info: { cls: 'bg-info/10 text-info', glyph: 'i' },
};

export function Badge({ tone = 'neutral', children }: { tone?: Tone; children: ReactNode }) {
  const t = tones[tone];
  return (
    <span className={cn('inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-sm font-medium', t.cls)}>
      <span aria-hidden="true">{t.glyph}</span>
      {children}
    </span>
  );
}
