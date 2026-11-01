import { cn } from '../lib/cn';

/** Placeholder block while data loads. Hidden from screen readers; announce loading on the container instead. */
export function Skeleton({ className }: { className?: string }) {
  return <div aria-hidden="true" className={cn('animate-pulse rounded-ui bg-fg/10 motion-reduce:animate-none', className)} />;
}
