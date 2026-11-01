import { useState } from 'react';

type Theme = 'light' | 'dark';

function currentTheme(): Theme {
  const set = document.documentElement.dataset.theme;
  if (set === 'light' || set === 'dark') return set;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>(currentTheme);

  function toggle() {
    const next: Theme = theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem('theme', next);
    } catch {
      /* storage can be blocked (private mode, sandboxed iframes): the toggle still works for this visit */
    }
    setTheme(next);
  }

  return (
    <button
      type="button"
      onClick={toggle}
      aria-pressed={theme === 'dark'}
      className="inline-flex min-h-11 items-center gap-2 rounded-ui ui-border border-line-strong bg-surface px-4 text-sm font-medium text-fg transition-colors hover:bg-raised"
    >
      <span aria-hidden="true">{theme === 'dark' ? '☾' : '☀'}</span>
      Dark mode
    </button>
  );
}
