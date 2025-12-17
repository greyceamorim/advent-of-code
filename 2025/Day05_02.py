from typing import List, Tuple

def parse_ranges_only(filename: str) -> List[Tuple[int, int]]:
    """
    Reads the input file and returns only the fresh ranges section.
    The file format is:
      - ranges (one per line, "a-b")
      - blank line
      - available IDs (ignored in Part 2)
    """
    ranges = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Stop at the blank line: Part 2 ignores the second section completely
            if line == "":
                break

            # Parse "a-b"
            a_str, b_str = line.split("-")
            a = int(a_str)
            b = int(b_str)

            # Normalise (just in case)
            if a > b:
                a, b = b, a

            ranges.append((a, b))

    return ranges


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merges overlapping ranges (and also ranges that touch, e.g. 5-10 and 11-20).
    After merging, the list represents the union of all fresh IDs.
    """
    if not ranges:
        return []

    # Sort by start
    ranges.sort(key=lambda x: x[0])

    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        # If the next range overlaps OR touches the current one, merge them.
        # "touches" means start == cur_end + 1 (no gap between integers)
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))
    return merged


def count_fresh_ids(merged: List[Tuple[int, int]]) -> int:
    """
    Counts how many integer IDs are covered by the merged ranges.
    Ranges are inclusive, so size = end - start + 1.
    """
    total = 0
    for start, end in merged:
        total += (end - start + 1)
    return total


def solve_day05_part2(filename: str) -> int:
    ranges = parse_ranges_only(filename)
    merged = merge_ranges(ranges)
    return count_fresh_ids(merged)


# --------------------
# TESTS (run these first)
# --------------------
def test_example():
    # Example ranges from the prompt (Part 2)
    ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
    merged = merge_ranges(ranges)
    total = count_fresh_ids(merged)

    print("\n\nSample for small tests \n\nMerged ranges (expected [(3,5),(10,20)]):", merged)
    print("Total fresh IDs (expected 14) from the sample:", total)

test_example()

# --------------------
# REAL INPUT
# --------------------
print("\n\n\nNow the real input for Day 5 - Part 2 answer: (☞ﾟ∀ﾟ)☞  ", solve_day05_part2("input_day05.txt"))
