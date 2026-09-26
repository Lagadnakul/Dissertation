/**
 * `doctor` — everything that must be true before a single token is spent.
 *
 * The original study's failures were nearly all of this kind: a model id that
 * had silently changed, a patch format the harness would never accept, a quota
 * that ran out mid-arm, a sampling parameter that was never set. None of those
 * are visible in a result file; all of them are visible here, in seconds, for
 * free.
 *
 * Every check prints PASS, FAIL or SKIP with the evidence. A FAIL on a gate
 * check exits non-zero, because a sweep launched over a broken gate produces
 * data that looks real and is not.
 */

import { loadConfig, keyStatus, type Config, type ProviderConfig } from "@rb/core";
import { toPatch, toUnifiedDiff, patchTargets } from "./edits/toPatch.ts";
import { checkApply, withScratchRepo, applyAndRead } from "./verify/apply.ts";

type Status = "PASS" | "FAIL" | "SKIP" | "WARN";

interface Check {
  name: string;
  status: Status;
  detail: string;
  /** A failing gate stops the run; a failing non-gate is reported and tolerated. */
  gate: boolean;
}

const checks: Check[] = [];
const record = (c: Check) => {
  checks.push(c);
  const mark = { PASS: "PASS", FAIL: "FAIL", SKIP: "SKIP", WARN: "WARN" }[c.status];
  console.log(`  ${mark}  ${c.name}`);
  for (const line of c.detail.split("\n")) {
    if (line.trim()) console.log(`        ${line}`);
  }
};

// ══════════════════════════════════════════════════ gate 1 · the patch format

/**
 * **The step-1 gate.** Prove `git apply` accepts what jsdiff emits.
 *
 * This is the single assumption the whole fairness retrofit rests on: the model
 * hands us SEARCH/REPLACE blocks, we compute the unified diff, and git must take
 * it. If jsdiff's header shape or hunk arithmetic disagreed with git's parser,
 * every APPLY_FAIL in the results would be our bug masquerading as a model
 * limitation — the exact confound the thesis criticises elsewhere.
 *
 * Tested on a file with the properties that actually break diff generation:
 * two hunks far apart, a trailing newline, an indentation-only line, and a
 * non-ASCII character.
 */
async function gatePatchFormat(): Promise<void> {
  const path = "astropy/modeling/separable.py";

  const before = [
    "import numpy as np",
    "",
    "",
    "def _coord_matrix(model, pos, noutp):",
    '    """Compute the coordinate matrix — see § separability."""',
    "    if isinstance(model, Mapping):",
    "        axes = []",
    "        for i in model.mapping:",
    "            axis = np.zeros((model.n_inputs,))",
    "            axis[i] = 1",
    "            axes.append(axis)",
    "        m = np.vstack(axes)",
    "        mat = np.zeros((noutp, model.n_inputs))",
    "        if pos == 'left':",
    "            mat[: model.n_outputs, : model.n_inputs] = m",
    "        else:",
    "            mat[-model.n_outputs :, -model.n_inputs :] = m",
    "        return mat",
    "    if not model.separable:",
    "        mat = np.zeros((noutp, model.n_inputs))",
    "        if pos == 'left':",
    "            mat[: model.n_outputs, : model.n_inputs] = 1",
    "        else:",
    "            mat[-model.n_outputs :, -model.n_inputs :] = 1",
    "    else:",
    "        mat = np.zeros((noutp, model.n_inputs))",
    "        for i in range(model.n_inputs):",
    "            mat[i, i] = 1",
    "        if pos == 'right':",
    "            mat = np.roll(mat, (noutp - model.n_outputs))",
    "    return mat",
    "",
    "",
    "def _cstack(left, right):",
    "    noutp = _compute_n_outputs(left, right)",
    "    if isinstance(left, Model):",
    "        cleft = _coord_matrix(left, 'left', noutp)",
    "    else:",
    "        cleft = np.zeros((noutp, left.shape[1]))",
    "        cleft[: left.shape[0], : left.shape[1]] = left",
    "    if isinstance(right, Model):",
    "        cright = _coord_matrix(right, 'right', noutp)",
    "    else:",
    "        cright = np.zeros((noutp, right.shape[1]))",
    "        cright[-right.shape[0] :, -right.shape[1] :] = 1",
    "    return np.hstack([cleft, cright])",
    "",
  ].join("\n");

  // Two changes, ~30 lines apart, so jsdiff must emit two separate @@ hunks.
  const after = before
    .replace("        return mat\n    if not model.separable:", "        return mat\n\n    if not model.separable:")
    .replace(
      "        cright[-right.shape[0] :, -right.shape[1] :] = 1",
      "        cright[-right.shape[0] :, -right.shape[1] :] = right",
    );

  if (after === before) {
    record({
      name: "jsdiff → git apply",
      status: "FAIL",
      detail: "the gate's own fixture failed to change; the test is broken",
      gate: true,
    });
    return;
  }

  const patch = toPatch([{ path, before, after }]);
  const hunks = (patch.match(/^@@ /gm) ?? []).length;
  const targets = patchTargets(patch);

  const result = await withScratchRepo({ [path]: before }, async (dir) => {
    const check = await checkApply(dir, patch);
    if (!check.ok) return { check, applied: null };
    const applied = await applyAndRead(dir, patch, path);
    return { check, applied };
  });

  if (!result.check.ok) {
    record({
      name: "jsdiff → git apply",
      status: "FAIL",
      detail:
        `git apply --check REJECTED a diff we generated. The fairness retrofit\n` +
        `cannot proceed — every APPLY_FAIL would be our bug, not the model's.\n` +
        `git said: ${result.check.stderr}\n` +
        `patch head:\n${patch.split("\n").slice(0, 6).join("\n")}`,
      gate: true,
    });
    return;
  }

  // Applying cleanly is not enough — it must produce the intended content.
  if (result.applied?.content !== after) {
    record({
      name: "jsdiff → git apply",
      status: "FAIL",
      detail:
        "the patch applied but the result does not equal the intended file.\n" +
        "A diff that applies to the wrong thing is worse than one that fails.",
      gate: true,
    });
    return;
  }

  record({
    name: "jsdiff → git apply",
    status: "PASS",
    detail:
      `${hunks} hunks across ${targets.length} file; applied clean and byte-exact\n` +
      `target resolved as ${targets[0]} (a/ b/ prefixes accepted at -p1)`,
    gate: true,
  });

  // A one-line change is the common case and has its own edge: a hunk at EOF.
  const eofPatch = toUnifiedDiff({
    path,
    before,
    after: before.replace("import numpy as np", "import numpy as np  # noqa"),
  });
  const eofOk = await withScratchRepo({ [path]: before }, (dir) =>
    checkApply(dir, eofPatch),
  );
  record({
    name: "jsdiff → git apply (single-hunk, file start)",
    status: eofOk.ok ? "PASS" : "FAIL",
    detail: eofOk.ok ? "accepted" : eofOk.stderr,
    gate: true,
  });
}

// ══════════════════════════════════════════════════ gate 2 · the frozen dataset

async function gateDataset(cfg: Config): Promise<void> {
  const metaPath = "data/swebench_lite.meta.json";
  const meta = await Bun.file(metaPath)
    .json()
    .catch(() => null);

  if (!meta) {
    record({
      name: "frozen dataset",
      status: "FAIL",
      detail: `${metaPath} missing — run: bun scripts/export_dataset.ts`,
      gate: true,
    });
    return;
  }

  const text = await Bun.file(cfg.tasks.source).text();
  const lines = text.split("\n").filter((l) => l.length > 0);
  const ids = new Set<string>();
  for (const l of lines) ids.add(JSON.parse(l).instance_id as string);

  const problems: string[] = [];
  if (lines.length !== cfg.tasks.expectedRows) {
    problems.push(`${lines.length} rows, config expects ${cfg.tasks.expectedRows}`);
  }
  if (ids.size !== lines.length) {
    problems.push(`${lines.length - ids.size} duplicate instance_id`);
  }
  if (meta.revision !== cfg.tasks.revision) {
    problems.push(
      `revision drift — file is ${meta.revision}, config pins ${cfg.tasks.revision}`,
    );
  }

  record({
    name: "frozen dataset",
    status: problems.length === 0 ? "PASS" : "FAIL",
    detail:
      problems.length === 0
        ? `${lines.length} instances, revision ${String(meta.revision).slice(0, 12)}…`
        : problems.join("\n"),
    gate: true,
  });

  // Every task the grid names must exist in the frozen file.
  const missing: string[] = [];
  for (const [name, set] of Object.entries(cfg.tasks.sets)) {
    for (const id of set.ids) if (!ids.has(id)) missing.push(`${name}: ${id}`);
  }
  record({
    name: "task sets resolve",
    status: missing.length === 0 ? "PASS" : "FAIL",
    detail:
      missing.length === 0
        ? `${Object.keys(cfg.tasks.sets).length} sets, all ids present`
        : `not in the dataset:\n${missing.join("\n")}`,
    gate: true,
  });
}

// ══════════════════════════════════════════════════════════ keys and providers

/** Reports presence only. A key value is never read, printed or logged. */
function checkKeys(cfg: Config): void {
  const lines: string[] = [];
  let anyMissing = false;
  for (const [id, p] of Object.entries(cfg.providers)) {
    for (const { name, present } of keyStatus(p)) {
      lines.push(`${present ? "set  " : "UNSET"}  ${name}  → provider ${id}`);
      if (!present) anyMissing = true;
    }
  }
  record({
    name: "API key env vars",
    status: anyMissing ? "WARN" : "PASS",
    detail:
      lines.join("\n") +
      (anyMissing
        ? "\nunset names are skipped when probing; load .env.local first"
        : ""),
    gate: false,
  });
}

interface Probe {
  model: string;
  ok: boolean;
  ttftMs: number | null;
  tps: number | null;
  completionTokens: number | null;
  reasoningTokens: number | null;
  error: string | null;
}

/**
 * Measures each endpoint rather than trusting its name.
 *
 * This check exists because the model names lie. In the screenshots that set the
 * model choice, "Flash" measured 13 tokens/s with a 24-second time-to-first-token
 * while a 550B model managed 164 tokens/s at 1.65s, and "Lightning" took 65
 * seconds to start with two samples disagreeing by 2×. Any budget or runtime
 * estimate built on the names would be wrong by an order of magnitude.
 */
async function probeModel(
  modelId: string,
  cfg: Config,
): Promise<Probe> {
  const m = cfg.models[modelId]!;
  const p: ProviderConfig = cfg.providers[m.provider]!;
  const keyName = p.apiKeyEnv.find((n) => (process.env[n] ?? "").length > 0);

  const base: Probe = {
    model: modelId,
    ok: false,
    ttftMs: null,
    tps: null,
    completionTokens: null,
    reasoningTokens: null,
    error: null,
  };

  if (!keyName) return { ...base, error: `no key set (${p.apiKeyEnv.join(", ")})` };
  if (p.kind !== "openai_compat") {
    return { ...base, error: `probe not implemented for kind ${p.kind}` };
  }

  const started = Bun.nanoseconds();
  let firstToken: number | null = null;

  try {
    const res = await fetch(`${p.baseUrl}/chat/completions`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        authorization: `Bearer ${process.env[keyName]}`,
      },
      body: JSON.stringify({
        model: m.model,
        messages: [
          { role: "user", content: "Reply with exactly: ok" },
        ],
        temperature: m.temperature,
        top_p: m.topP,
        max_tokens: 16,
        stream: true,
        stream_options: { include_usage: true },
      }),
      signal: AbortSignal.timeout(p.timeoutS * 1000),
    });

    if (!res.ok) {
      const body = (await res.text()).slice(0, 200);
      return { ...base, error: `HTTP ${res.status} — ${body}` };
    }

    /** Providers disagree on where reasoning tokens live; read both shapes. */
    type Usage = {
      completion_tokens?: number;
      reasoning_tokens?: number;
      completion_tokens_details?: { reasoning_tokens?: number };
    };
    let usage: Usage | null = null;
    const reader = res.body!.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split("\n");
      buffer = parts.pop() ?? "";
      for (const line of parts) {
        if (!line.startsWith("data: ")) continue;
        const payload = line.slice(6).trim();
        if (payload === "[DONE]") continue;
        const chunk = JSON.parse(payload);
        if (firstToken === null && chunk.choices?.[0]?.delta?.content) {
          firstToken = Bun.nanoseconds();
        }
        if (chunk.usage) usage = chunk.usage;
      }
    }

    const endedMs = (Bun.nanoseconds() - started) / 1e6;
    const ttftMs = firstToken === null ? null : (firstToken - started) / 1e6;
    const completion = usage?.completion_tokens ?? null;
    const reasoning =
      usage?.completion_tokens_details?.reasoning_tokens ??
      usage?.reasoning_tokens ??
      null;

    return {
      model: modelId,
      ok: true,
      ttftMs,
      tps:
        completion !== null && ttftMs !== null && endedMs > ttftMs
          ? completion / ((endedMs - ttftMs) / 1000)
          : null,
      completionTokens: completion,
      reasoningTokens: reasoning,
      error: null,
    };
  } catch (e) {
    return { ...base, error: e instanceof Error ? e.message : String(e) };
  }
}

async function checkProviders(cfg: Config, live: boolean): Promise<void> {
  const modelIds = [
    ...new Set(
      Object.values(cfg.grid)
        .filter((a) => a.enabled)
        .flatMap((a) => a.models),
    ),
  ].sort();

  if (!live) {
    record({
      name: "endpoint probe",
      status: "SKIP",
      detail:
        `${modelIds.length} models in enabled arms; pass --live to measure them.\n` +
        `Names are not evidence: TPS and TTFT must be measured, not assumed.`,
      gate: false,
    });
    return;
  }

  const probes = await Promise.all(modelIds.map((id) => probeModel(id, cfg)));
  const lines = probes.map((p) => {
    if (!p.ok) return `FAIL  ${p.model}  ${p.error}`;
    const ttft = p.ttftMs === null ? "  n/a" : `${(p.ttftMs / 1000).toFixed(2)}s`;
    const tps = p.tps === null ? " n/a" : p.tps.toFixed(1);
    const think =
      p.reasoningTokens === null
        ? ""
        : `  ⚠ billed ${p.reasoningTokens} reasoning tokens`;
    return `ok    ${p.model.padEnd(22)} ttft ${ttft}  ${tps} tok/s${think}`;
  });

  // D5: a model configured thinking:false that still bills reasoning tokens is a
  // validity threat, not a cost surprise — it silently breaks the comparison.
  const leaking = probes.filter(
    (p) => p.ok && (p.reasoningTokens ?? 0) > 0 && !cfg.models[p.model]!.thinking,
  );
  if (leaking.length > 0) {
    lines.push(
      "",
      "D5 VIOLATION: these models bill reasoning tokens despite thinking: false —",
      "the Reflection-only comparison is not valid against them:",
      ...leaking.map((p) => `  ${p.model}`),
    );
  }

  const failed = probes.filter((p) => !p.ok).length;
  record({
    name: "endpoint probe",
    status: leaking.length > 0 ? "FAIL" : failed > 0 ? "WARN" : "PASS",
    detail: lines.join("\n"),
    gate: leaking.length > 0,
  });
}

// ══════════════════════════════════════════════════════════════ sampling pins

function checkSamplingPins(cfg: Config): void {
  const lines = Object.entries(cfg.models).map(
    ([id, m]) =>
      `${id.padEnd(22)} temp ${m.temperature}  top_p ${m.topP}  ` +
      `thinking ${m.thinking}  max_tokens ${m.maxTokens}`,
  );
  record({
    name: "sampling pinned",
    status: "PASS",
    detail:
      `seed ${cfg.run.seed}\n` +
      lines.join("\n") +
      `\nzod requires temperature and top_p — there is no default, so the ` +
      `original's\nunpinned sampling cannot recur silently.`,
    gate: false,
  });
}

// ══════════════════════════════════════════════════════════════════════ main

export async function doctor(configPath: string, live: boolean): Promise<number> {
  console.log(`\nrecovery-bench doctor`);
  console.log(`config  ${configPath}${live ? "   (live probes enabled)" : ""}\n`);

  let cfg: Config;
  let hash: string;
  try {
    const loaded = await loadConfig(configPath);
    cfg = loaded.config;
    hash = loaded.hash;
  } catch (e) {
    console.log(`  FAIL  config\n        ${e instanceof Error ? e.message : e}\n`);
    return 1;
  }
  record({
    name: "config",
    status: "PASS",
    detail:
      `hash ${hash}  ·  run "${cfg.run.name}"  ·  verify ${cfg.verify.backend}\n` +
      `${Object.keys(cfg.models).length} models, ` +
      `${Object.keys(cfg.grid).length} arms ` +
      `(${Object.values(cfg.grid).filter((a) => a.enabled).length} enabled)`,
    gate: true,
  });

  await gatePatchFormat();
  await gateDataset(cfg);
  checkSamplingPins(cfg);
  checkKeys(cfg);
  await checkProviders(cfg, live);

  const failedGates = checks.filter((c) => c.gate && c.status === "FAIL");
  const warns = checks.filter((c) => c.status === "WARN").length;

  console.log("");
  if (failedGates.length > 0) {
    console.log(
      `${failedGates.length} gate check(s) FAILED — a sweep launched now would ` +
        `produce data that looks real and is not:`,
    );
    for (const c of failedGates) console.log(`  · ${c.name}`);
    console.log("");
    return 1;
  }
  console.log(
    `all gates pass${warns > 0 ? `, ${warns} warning(s)` : ""} — safe to sweep.`,
  );
  console.log("");
  return 0;
}
