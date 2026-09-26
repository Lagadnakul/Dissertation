/**
 * The contract. Imported by the pipeline (which writes these) and the dashboard
 * (which renders them), so the two cannot drift — a change here breaks the
 * dashboard build rather than producing a silently wrong chart.
 *
 * Nothing in this file imports anything. It is types and constants only.
 */

// --------------------------------------------------------------------- cells

export const EDIT_FORMATS = ["search_replace", "unified_diff"] as const;
export type EditFormat = (typeof EDIT_FORMATS)[number];

export const STRATEGY_IDS = [
  "l0_baseline",
  "l1_blind_retry",
  "l2_reflection",
  "l2_5_diagnose_revise",
  "l3_constrained",
  "l4_tool_grounded",
] as const;
export type StrategyId = (typeof STRATEGY_IDS)[number];

/** Model ids are config-defined, so this stays a branded string, not a union. */
export type ModelId = string;

/**
 * The unit of work. Cell identity is the full tuple — ARCHITECTURE §2.
 * The grid is enumerated from config before any call is made, so every cell
 * that will ever exist is known up front.
 */
export interface Cell {
  taskId: string;
  strategy: StrategyId;
  model: ModelId;
  editFormat: EditFormat;
  thinking: boolean;
  round: number;
  repeat: number;
}

/** Stable, order-independent key. Used for queue identity and dedup. */
export function cellKey(c: Cell): string {
  return [
    c.taskId,
    c.strategy,
    c.model,
    c.editFormat,
    c.thinking ? "think" : "nothink",
    `r${c.round}`,
    `n${c.repeat}`,
  ].join("|");
}

// ------------------------------------------------------------------ outcomes

/**
 * The terminal taxonomy, no-Docker version (D6).
 *
 * `RESOLVED` / `UNRESOLVED` are deliberately absent: they require test
 * execution, which this project does not do. They exist only on replayed
 * historical rows, which carry `verification: "test"`.
 */
export const OUTCOME_KINDS = [
  "NO_OUTPUT",
  "NO_PATCH",
  "MALFORMED",
  "APPLY_FAIL",
  "APPLIED",
  "CONTAMINATED",
  "PROVIDER_ERROR",
  "BUDGET_STOP",
] as const;
export type OutcomeKind = (typeof OUTCOME_KINDS)[number];

/**
 * Why a `MALFORMED` outcome is malformed.
 *
 * `MALFORMED` without a reason is a dead end in the results — every failure looks
 * the same, and a model that misremembered one space of indentation is scored
 * identically to one that invented a function. These reasons make the two
 * separable at analysis time, which is the whole point of the layer.
 *
 * The first three mirror the legacy statuses in `apply_log_v2.json`
 * (`search_not_found`, `search_ambiguous`, `applied_ok`) so archived rows and new
 * rows use one vocabulary.
 */
export const MALFORMED_REASONS = [
  // SEARCH/REPLACE path
  "search_not_found", //        exact match absent from the file
  "search_not_found_whitespace", // would have matched if whitespace were normalised
  "search_ambiguous", //        more than one match — unsafe to choose
  "search_empty", //            empty SEARCH body
  "block_unterminated", //      <<<<<<< with no ======= or >>>>>>>
  // unified-diff path
  "no_file_header", //          no --- / +++ pair, so git cannot know the target
  "hunk_count_mismatch", //     declared @@ ,n counts disagree with the body
  "hunk_header_unparseable",
] as const;
export type MalformedReason = (typeof MALFORMED_REASONS)[number];

/**
 * Every variant carries the evidence for its own classification. This is the
 * property the original code lacked: a rejected patch printed `Not applied`
 * and wrote nothing, so 8 of 24 cells ceased to exist (PLAN.md D2).
 */
export type Outcome =
  | { kind: "NO_OUTPUT"; detail: string }
  | { kind: "NO_PATCH"; responseChars: number }
  | {
      kind: "MALFORMED";
      reason: MalformedReason;
      /** 0-based block or hunk index, or -1 when the defect is file-level. */
      blockIndex: number;
      /** The SEARCH body, or the offending hunk header. Truncated by the writer. */
      searchText: string;
      /** 1-based line where a near-match was found, when one was. */
      nearestLine: number | null;
      detail: string;
    }
  | { kind: "APPLY_FAIL"; patch: string; gitStderr: string }
  | { kind: "APPLIED"; patch: string; filesChanged: string[] }
  | { kind: "CONTAMINATED"; patch: string; similarity: number; threshold: number }
  | { kind: "PROVIDER_ERROR"; status: number | null; reason: string; retries: number }
  | { kind: "BUDGET_STOP"; tokensUsed: number; ceiling: number };

/** True when the model produced a patch git accepted at `base_commit`. */
export function isApplied(o: Outcome): boolean {
  return o.kind === "APPLIED" || o.kind === "CONTAMINATED";
}

/** Outcomes where the patch never reached the repository — "format-class". */
export function isFormatClass(o: Outcome): boolean {
  return o.kind === "MALFORMED" || o.kind === "APPLY_FAIL" || o.kind === "NO_PATCH";
}

// -------------------------------------------------------------- verification

/**
 * The integrity rule, as a type.
 *
 * `"test"` rows came out of the SWE-bench Docker harness and exist only in the
 * archive — 73 of them, and there will never be another (D6).
 * `"apply"` rows are everything this pipeline produces.
 *
 * Mixing them would let a resolve rate be computed over rows that were never
 * tested. Making verification a type parameter means that mistake fails to
 * compile instead of failing review.
 */
export type Verification = "test" | "apply";

export interface Usage {
  promptTokens: number;
  completionTokens: number;
  /** Non-null only when the model billed reasoning separately (D5 confound). */
  reasoningTokens: number | null;
  latencyMs: number;
}

export interface Row<V extends Verification> {
  cell: Cell;
  verification: V;
  outcome: Outcome;
  /** Present only on test-verified rows; `null` is not a legal value for V="test". */
  resolved: V extends "test" ? boolean : null;
  /** Sub-test detail from report.json — archive rows only. */
  tests: V extends "test"
    ? { f2pPassed: number; f2pTotal: number; p2pPassed: number; p2pTotal: number }
    : null;
  usage: Usage | null;
  runId: string;
  timestamp: string;
}

export type AnyRow = Row<"test"> | Row<"apply">;

/** Narrows a mixed list. The only sanctioned way to get at historical rows. */
export function testRows(rows: AnyRow[]): Row<"test">[] {
  return rows.filter((r): r is Row<"test"> => r.verification === "test");
}

export function applyRows(rows: AnyRow[]): Row<"apply">[] {
  return rows.filter((r): r is Row<"apply"> => r.verification === "apply");
}

/**
 * Resolve rate is only definable over test-verified rows. The signature is the
 * guard: there is no overload that accepts `Row<"apply">`.
 */
export function resolveRate(rows: Row<"test">[]): number {
  if (rows.length === 0) return NaN;
  return rows.filter((r) => r.resolved).length / rows.length;
}

/** Apply rate is the headline metric of the new work. */
export function applyRate(rows: Row<"apply">[]): number {
  if (rows.length === 0) return NaN;
  return rows.filter((r) => isApplied(r.outcome)).length / rows.length;
}

// ------------------------------------------------------------------- tasks

export interface Task {
  instanceId: string;
  repo: string;
  baseCommit: string;
  environmentSetupCommit: string;
  problemStatement: string;
  /** The gold patch. Used for contamination scoring only, never shown to a model. */
  patch: string;
  testPatch: string;
  failToPass: string[];
  passToPass: string[];
  version: string;
}
