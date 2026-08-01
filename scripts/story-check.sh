#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"
cd "${repo_root}"

required=(AGENTS.md README.md CANON.md PUBLISHING.md continuity/now.md continuity/time-map.md continuity/story-map.md continuity/frontier.md publishing/schedule.json)
for path in "${required[@]}"; do
  if [[ ! -s "${path}" ]]; then
    printf 'ERROR missing required state file: %s\n' "${path}" >&2
    exit 1
  fi
done

shopt -s nullglob
stories=(stories/[0-9][0-9]-*.md)
if (( ${#stories[@]} == 0 )); then
  printf 'ERROR no numbered story files found\n' >&2
  exit 1
fi

expected=0
warnings=0
total_words=0

for path in "${stories[@]}"; do
  file="${path##*/}"
  number="${file%%-*}"
  value=$((10#${number}))

  if (( value != expected )); then
    printf 'ERROR chapter sequence expected %02d but found %s in %s\n' "${expected}" "${number}" "${path}" >&2
    exit 1
  fi

  heading_count="$(grep -c '^# ' "${path}" || true)"
  if [[ "${heading_count}" != "1" ]]; then
    printf 'ERROR expected one H1 title in %s; found %s\n' "${path}" "${heading_count}" >&2
    exit 1
  fi

  words="$(wc -w < "${path}")"
  total_words=$((total_words + words))
  if (( words < 500 || words > 4000 )); then
    printf 'WARN unusual chapter length: %s words in %s\n' "${words}" "${path}"
    warnings=$((warnings + 1))
  fi

  expected=$((expected + 1))
done

git diff --check

printf 'OK %d contiguous chapters (00-%02d), %d words, %d warnings\n' "${#stories[@]}" "$((expected - 1))" "${total_words}" "${warnings}"
