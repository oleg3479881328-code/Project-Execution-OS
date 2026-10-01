from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KeywordRule:
    keyword: str
    match_mode: str = "contains"
    case_sensitive: bool = False


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def find_matching_keywords(
    *,
    title: str,
    body: str,
    rules: list[KeywordRule],
) -> tuple[str, ...]:
    source = f"{title}\n{body}"
    matches: list[str] = []

    for rule in rules:
        keyword = rule.keyword.strip()
        if not keyword:
            continue

        haystack = source if rule.case_sensitive else source.casefold()
        needle = keyword if rule.case_sensitive else keyword.casefold()

        if rule.match_mode == "contains":
            matched = needle in haystack
        elif rule.match_mode == "phrase":
            matched = _normalize_whitespace(needle) in _normalize_whitespace(haystack)
        elif rule.match_mode == "exact":
            matched = bool(re.search(rf"(?<!\w){re.escape(needle)}(?!\w)", haystack))
        else:
            raise ValueError(f"Unsupported match mode: {rule.match_mode}")

        if matched:
            matches.append(rule.keyword)

    return tuple(dict.fromkeys(matches))
