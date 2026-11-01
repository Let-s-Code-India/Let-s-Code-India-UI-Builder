import type { ReactNode } from 'react';

/** An empty screen is an invitation to act: say what is missing and offer the next step. */
export function EmptyState({ title, children, action }: { title: string; children: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex flex-col items-start gap-3 rounded-ui-lg ui-border border-dashed border-line-strong p-8">
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="max-w-prose text-muted">{children}</p>
      {action}
    </div>
  );
}
