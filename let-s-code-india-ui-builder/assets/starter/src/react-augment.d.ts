// Invoker Commands (command / commandfor) are Baseline since Dec 2025 but not yet in @types/react.
import 'react';

declare module 'react' {
  interface ButtonHTMLAttributes<T> {
    command?: 'show-modal' | 'close' | 'request-close' | 'show-popover' | 'hide-popover' | 'toggle-popover' | `--${string}`;
    commandfor?: string;
  }
}

declare module 'react' {
  // <dialog closedby="any|closerequest|none"> - light-dismiss control (Chromium/Firefox; Safari ignores it gracefully).
  interface DialogHTMLAttributes<T> {
    closedby?: 'any' | 'closerequest' | 'none';
  }
}
