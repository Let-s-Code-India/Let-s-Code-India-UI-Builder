#!/usr/bin/env node
/**
 * check_classes.mjs - verify that every Tailwind class in your source really exists.
 *
 * Uses the project's own Tailwind v4 compiler (via @tailwindcss/node, installed with
 * @tailwindcss/vite), so custom tokens from your @theme (bg-canvas, rounded-ui, ...) are
 * known and typos like "bg-zinc-850" are caught exactly.
 *
 * Usage (run from the project root, after `npm install`):
 *   node path/to/check_classes.mjs src index.html
 *   node path/to/check_classes.mjs src --css src/index.css --allow btn,card-x
 *
 * Exit code: 0 = all classes valid, 1 = invalid class found, 2 = setup problem.
 */
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, extname, dirname, resolve } from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const paths = [];
let cssEntry = null;
let allow = new Set();
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--css') cssEntry = args[++i];
  else if (args[i] === '--allow') allow = new Set(args[++i].split(',').map((s) => s.trim()).filter(Boolean));
  else paths.push(args[i]);
}
if (paths.length === 0) {
  console.error('usage: node check_classes.mjs <files|dirs...> [--css src/index.css] [--allow class1,class2]');
  process.exit(2);
}

const EXT = new Set(['.tsx', '.jsx', '.ts', '.js', '.html', '.htm', '.vue', '.svelte', '.astro']);
const SKIP = new Set(['node_modules', 'dist', 'build', '.git', '.next', '.vite']);

function walk(p, out = []) {
  if (!existsSync(p)) return out;
  const st = statSync(p);
  if (st.isDirectory()) {
    for (const name of readdirSync(p)) if (!SKIP.has(name)) walk(join(p, name), out);
  } else if (EXT.has(extname(p).toLowerCase())) out.push(p);
  return out;
}

const cwdRequire = createRequire(join(process.cwd(), 'package.json'));
let compile;
try {
  ({ compile } = await import(pathToFileURL(cwdRequire.resolve('@tailwindcss/node')).href));
} catch {
  console.error('Cannot load @tailwindcss/node. Run `npm install -D tailwindcss @tailwindcss/vite` in the project first.');
  process.exit(2);
}

// CSS entry: the file that contains @import "tailwindcss" and your @theme
if (!cssEntry) cssEntry = ['src/index.css', 'src/styles.css', 'src/app.css', 'src/main.css', 'app/globals.css']
  .find((f) => existsSync(f));
const cssSource = cssEntry ? readFileSync(cssEntry, 'utf8') : '@import "tailwindcss";';
const base = cssEntry ? dirname(resolve(cssEntry)) : process.cwd();
const compiler = await compile(cssSource, { base, onDependency() {} });

// classes the project defines itself in plain CSS (.btn { ... })
const customClasses = new Set(allow);
for (const m of cssSource.matchAll(/\.([A-Za-z_][\w-]*)/g)) customClasses.add(m[1]);

const esc = (s) => s.replace(/[^a-zA-Z0-9_-]/g, (c) => '\\' + c);
const looksLikeClass = (t) => /^[!@a-z0-9\-[][^\s"'`<>]*$/.test(t) && !t.includes('${') && !/^https?:/.test(t) && t.length > 1;

const files = paths.flatMap((p) => walk(p));
const strings = []; // {file, line, text, forced}
for (const f of files) {
  const src = readFileSync(f, 'utf8');
  const lineAt = (idx) => src.slice(0, idx).split('\n').length;
  const forced = [];
  for (const m of src.matchAll(/\bclass(?:Name)?\s*=\s*(?:\{\s*)?(["'`])((?:\\.|(?!\1)[^\\])*)\1/gs)) {
    forced.push(m.index);
    strings.push({ file: f, line: lineAt(m.index), text: m[2], forced: true });
  }
  for (const m of src.matchAll(/(["'`])((?:\\.|(?!\1)[^\\\n])*)\1/g)) {
    if (forced.some((i) => Math.abs(i - m.index) < 14)) continue;
    strings.push({ file: f, line: lineAt(m.index), text: m[2], forced: false });
  }
}

const candidates = new Set();
for (const s of strings) for (const t of s.text.split(/\s+/)) if (looksLikeClass(t)) candidates.add(t);
const css = compiler.build([...candidates]);
const valid = new Set([...candidates].filter((c) => css.includes('.' + esc(c))));

let bad = 0;
for (const s of strings) {
  const toks = s.text.split(/\s+/).filter(Boolean);
  const hit = toks.filter((t) => valid.has(t)).length;
  if (!s.forced && !(hit >= 1 && hit / toks.length >= 0.5)) continue;
  for (const t of toks) {
    if (!looksLikeClass(t) || valid.has(t) || customClasses.has(t)) continue;
    if (/^(group|peer|dark|light|container|sr-only|not-sr-only)$/.test(t)) continue;
    console.log(`${s.file}:${s.line}: invalid Tailwind class "${t}"`);
    bad++;
  }
}
console.log(`${files.length} files, ${valid.size} valid classes checked, ${bad} invalid`);
process.exit(bad ? 1 : 0);
