# Self-Reflection and Failure Recovery in Agentic AI Coding Systems

M.Tech dissertation — **Lagad Nakul Kiran** (2503032340022)
Artificial Intelligence & Data Science, PIET, Parul University

When an LLM's first attempt at a code patch fails, what should it do next? This
work builds an evaluation harness that measures three answers against each
other on real SWE-bench Lite tasks: retry blindly, reflect on the failure first,
or diagnose then revise.

---

## What is here

| Path | Contents |
|------|----------|
| [`thesis/`](thesis/) | The dissertation itself — `Self.docx` (submitted), `Self.pdf`, and the M.Tech report |
| [`recovery-bench/`](recovery-bench/) | The implementation — TypeScript on Bun, 433 tests |
| [`reports/`](reports/) | Generated figures, chapter data, and weekly progress reports |
| [`explainer/`](explainer/) | A static walkthrough of the build, phase by phase |
| [`literature/`](literature/) | The systematic review the research gap came from |
| [`PLAN.md`](PLAN.md) | The Phase II completion plan and decision log |

---

## The implementation

`recovery-bench/` is a Bun workspace with three packages:

| Package | Role |
|---------|------|
| `core` | Shared types, scrubbing, provider adapters |
| `pipeline` | The CLI — `try`, `replay`, `sweep`, `report`, `doctor` |
| `dashboard` | Vite + React + Tailwind results viewer |

**Stack:** TypeScript on Bun · zod · openai + @google/genai · jsdiff · plain git.
No charting library — the dashboard draws its own marks.

Design documents live in [`recovery-bench/docs/`](recovery-bench/docs/) and are
meant to be read in order: `DECISIONS.md` (D0–D33, every decision with its
evidence), then `ARCHITECTURE.md`, `CONFIG.md`, `BUDGET.md`, `DASHBOARD.md`.

### Three standing constraints

1. **Docker is never used** (D6).
2. **API key *values* are never read into this repository** — only variable
   names. `configs/` references secrets by name only (D3).
3. **`Self.docx` is submitted and is never edited.**

### Status

Steps 1–7 are built: 433 tests, 127 palette checks. Step 8 (`l3_constrained`,
`l4_tool_grounded`) is declared and not yet written.

---

## Running it

Requires [Bun](https://bun.sh).

```bash
cd recovery-bench
bun install

bun run doctor          # environment and config check
bun run replay          # re-run against committed fixtures, no API calls
bun run report          # regenerate reports/ data
```

Live runs need API keys. Copy `recovery-bench/.env.example` to `.env.local` at
the repository root and fill it in — that file is gitignored and its values are
never committed.

### The dashboard

```bash
cd recovery-bench
bun run --cwd packages/dashboard dev     # http://localhost:5178
```

The build copies the pipeline's committed data into the dashboard before
bundling, so `bun run build` must be used rather than `vite build` alone.

---

## Deployments

Both are static and deploy from this repository.

| Site | Root Directory | Build | Output |
|------|----------------|-------|--------|
| Explainer | `explainer` | none — static HTML | `.` |
| Dashboard | `recovery-bench` | `bun run --cwd packages/dashboard build` | `packages/dashboard/dist` |

Each directory carries a `vercel.json` with these settings.

> The dashboard's root is `recovery-bench`, **not** `packages/dashboard`. Its
> build reads `recovery-bench/data/` and aliases `@rb/core` to `packages/core`,
> both of which sit outside the dashboard package.

The dashboard is also built with `base: "./"` so the `dist/` folder opens
correctly from `file://` — it can be handed to an examiner as a plain folder
with no server.
