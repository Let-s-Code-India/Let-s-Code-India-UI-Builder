import { useId } from 'react';
import type { ReactNode } from 'react';
import { Button } from './Button';
import type { ButtonProps } from './Button';

const nativeInvokers = typeof HTMLButtonElement !== 'undefined' && 'commandForElement' in HTMLButtonElement.prototype;

/**
 * Opens the <dialog> with the given id as a modal.
 * Declarative (command/commandfor, Baseline Dec 2025); falls back to showModal() where unsupported.
 */
export function DialogTrigger({ dialogId, ...props }: Omit<ButtonProps, 'command' | 'commandfor'> & { dialogId: string }) {
  return (
    <Button
      command="show-modal"
      commandfor={dialogId}
      onClick={
        nativeInvokers
          ? undefined
          : () => (document.getElementById(dialogId) as HTMLDialogElement | null)?.showModal()
      }
      {...props}
    />
  );
}

interface DialogProps {
  id: string;
  title: string;
  children: ReactNode;
  /** Buttons rendered in the footer. Put the SAFE action first: it receives initial focus. */
  actions: ReactNode;
  /** Called with the value of the button used ('' for Esc / back gesture). */
  onClose?: (returnValue: string) => void;
}

/**
 * Native modal dialog. The browser already provides: inert page, focus containment,
 * top layer, ::backdrop, Esc / back-gesture dismissal and focus return to the trigger.
 * So: no role="dialog", no aria-modal, no focus-trap code.
 */
export function Dialog({ id, title, children, actions, onClose }: DialogProps) {
  const titleId = useId();
  return (
    <dialog
      id={id}
      aria-labelledby={titleId}
      closedby="any"
      onClose={(e) => {
        const dlg = e.currentTarget;
        onClose?.(dlg.returnValue);
        dlg.returnValue = ''; // reset so a stale value never leaks into the next close
      }}
    >
      <form method="dialog" className="flex flex-col gap-4 p-6">
        <h2 id={titleId} className="text-xl font-semibold">
          {title}
        </h2>
        <div className="text-muted">{children}</div>
        <div className="flex flex-wrap justify-end gap-3 pt-2">{actions}</div>
      </form>
    </dialog>
  );
}
