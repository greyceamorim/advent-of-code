from bisect import bisect_right


def parse_database(text: str) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Parse input format:
    - Fresh ranges: "a-b" lines
    - Blank line
    - Available IDs: one integer per line
    """
    lines = [line.rstrip("\n") for line in text.splitlines()]

    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    i = 0

    # --- Read ranges until blank line ---
    while i < len(lines) and lines[i].strip() != "":
        a_str, b_str = lines[i].split("-")
        a = int(a_str)
        b = int(b_str)
        if a > b:
            a, b = b, a  # safety: normalize if input is reversed
        ranges.append((a, b))
        i += 1

    # Skip blank line(s)
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    # --- Read IDs ---
    while i < len(lines):
        if lines[i].strip() != "":
            ids.append(int(lines[i].strip()))
        i += 1

    return ranges, ids


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merge overlapping (or touching) inclusive ranges.

    Example:
      (3,5) and (6,10) can be merged because 5 and 6 are adjacent,
      and ranges are inclusive -> they form a continuous fresh interval.
    """
    if not ranges:
        return []

    ranges_sorted = sorted(ranges)  # sort by start then end
    merged: list[tuple[int, int]] = []

    cur_start, cur_end = ranges_sorted[0]

    for start, end in ranges_sorted[1:]:
        if start <= cur_end + 1:
            # Overlap or adjacency -> extend current range
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))
    return merged


def count_fresh_ids(merged_ranges: list[tuple[int, int]], ids: list[int]) -> int:
    """
    Count how many ids fall inside any merged range using binary search.

    Strategy:
    - Extract starts in a list.
    - For an id x, find the last range with start <= x.
    - Then check if x <= that range's end.
    """
    if not merged_ranges:
        return 0

    starts = [a for a, _ in merged_ranges]
    fresh = 0

    for x in ids:
        idx = bisect_right(starts, x) - 1
        if idx >= 0:
            a, b = merged_ranges[idx]
            if a <= x <= b:
                fresh += 1

    return fresh


def solve(text: str) -> int:
    ranges, ids = parse_database(text)
    merged = merge_ranges(ranges)
    return count_fresh_ids(merged, ids)


# --------------------
# Tests (run these first)
# --------------------
example = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
print("Example with short list - (ღ˘⌣˘ღ) (expected answer 3):", solve(example))


# --------------------
# Real input from file
# --------------------
with open("input_day05.txt", "r") as f:
    real_text = f.read()

print("Day 5 - Part 1 answer ( •̀ ω •́ )✧:", solve(real_text))
