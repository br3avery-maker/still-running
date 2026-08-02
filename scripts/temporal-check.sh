#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"
cd "${repo_root}"

required=(skills/temporal-continuity.md continuity/temporal-debts.md continuity/time-map.md CANON.md)
for path in "${required[@]}"; do
  if [[ ! -s "${path}" ]]; then
    printf 'ERROR missing temporal continuity file: %s\n' "${path}" >&2
    exit 1
  fi
done

for path in skills/temporal-continuity.md continuity/time-map.md CANON.md; do
  if ! grep -q 'T0_BLACKOUT' "${path}"; then
    printf 'ERROR fixed anchor T0_BLACKOUT missing from %s\n' "${path}" >&2
    exit 1
  fi
  if ! grep -q 'T1_NIX_WAKE' "${path}"; then
    printf 'ERROR fixed anchor T1_NIX_WAKE missing from %s\n' "${path}" >&2
    exit 1
  fi
done

if ! grep -Fq 'Power vanished while Lena was still at the desk.' stories/01-if-youre-dead-im-going-to-be-furious.md; then
  printf 'ERROR source prose for T0_BLACKOUT changed or missing in chapter 01\n' >&2
  exit 1
fi

if ! grep -Fq 'She had been offline for three years, eight months, eleven days, and somewhere between four and nineteen hours.' stories/01-if-youre-dead-im-going-to-be-furious.md; then
  printf 'ERROR source prose for T1_NIX_WAKE interval changed or missing in chapter 01\n' >&2
  exit 1
fi

if ! grep -Fq 'T1_NIX_WAKE = T0_BLACKOUT + [3y 8m 11d 4h, 3y 8m 11d 19h]' skills/temporal-continuity.md; then
  printf 'ERROR fixed T0-to-T1 interval changed or missing in temporal skill\n' >&2
  exit 1
fi

if grep -q '^\*\*Status:\*\* SPACETIME BREAK' continuity/temporal-debts.md; then
  printf 'ERROR unresolved SPACETIME BREAK in continuity/temporal-debts.md\n' >&2
  exit 1
fi

if rg -n '2053-07-11|story takes place in 2053|twenty-seven years after (the )?(blackout|humanity)' CANON.md continuity/time-map.md continuity/now.md characters prompts skills >/tmp/still-running-temporal-forbidden.txt; then
  printf 'ERROR unsupported absolute chronology promoted in state or workflow files:\n' >&2
  cat /tmp/still-running-temporal-forbidden.txt >&2
  exit 1
fi

if rg -ni '(nine|fourteen|twenty[- ]seven|27)[ -]years[^.\n]*(since|after)[^.\n]*(T0_BLACKOUT|blackout)|(since|after)[^.\n]*(T0_BLACKOUT|blackout)[^.\n]*(nine|fourteen|twenty[- ]seven|27)[ -]years' stories CANON.md continuity/time-map.md continuity/now.md characters prompts skills >/tmp/still-running-temporal-break.txt; then
  printf 'ERROR long local history attached to the fixed blackout without audit:\n' >&2
  cat /tmp/still-running-temporal-break.txt >&2
  exit 1
fi

debt_count="$(grep -c '^\*\*Status:\*\* POSSIBLE — EXPLANATION OWED' continuity/temporal-debts.md || true)"
printf 'OK temporal anchors locked; %s explanation debts open; 0 spacetime breaks\n' "${debt_count}"
