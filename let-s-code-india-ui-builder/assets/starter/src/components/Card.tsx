import { createElement } from 'react';
import type { HTMLAttributes } from 'react';
import { cn } from '../lib/cn';

interface CardProps extends HTMLAttributes<HTMLElement> {
  as?: 'div' | 'section' | 'article' | 'li';
}

/** Surface container. Radius, border width and shadow come from the active data-style. */
export function Card({ as = 'div', className, ...rest }: CardProps) {
  return createElement(as, {
    className: cn(
      'ui-border rounded-ui-lg border-line bg-surface p-6 shadow-ui',
      'in-data-[style=glass]:bg-surface/60 in-data-[style=glass]:backdrop-blur-xl',
      className,
    ),
    ...rest,
  });
}
