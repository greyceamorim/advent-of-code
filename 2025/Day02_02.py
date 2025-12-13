print("Oieee! Day 2 - part 2\n\nLet's do this!")
print("\n              meow  ฅ^•ﻌ•^ฅ meow")
print("\nI am using ChatGPT to help me with the logic {•ᴗ•}♡\n\n")


from bisect import bisect_left, bisect_right

# ------------------------------------------------------------
# Generate all invalid IDs up to max_digits.
#
# An ID is invalid if it consists of a sequence of digits
# repeated AT LEAST twice.
#
# Examples:
#   11          -> "1" repeated 2 times
#   111         -> "1" repeated 3 times
#   6464        -> "64" repeated 2 times
#   123123123   -> "123" repeated 3 times
#
# Strategy:
#   - Generate all repeated-pattern numbers mathematically
#   - Store in a set to avoid duplicates
#   - Sort at the end
# ------------------------------------------------------------
def generate_invalid_ids(max_digits: int) -> list[int]:
    invalid = set()

    for block_len in range(1, max_digits + 1):
        # block repeated r times (r >= 2)
        for repeats in range(2, (max_digits // block_len) + 1):
            total_len = block_len * repeats
            if total_len > max_digits:
                continue

            # block must have exactly block_len digits (no leading zeros)
            lo = 10 ** (block_len - 1)
            hi = 10 ** block_len - 1

            # build factor = 111... pattern in base 10
            # Example: block_len=2, repeats=3 → 10101
            factor = 0
            for _ in range(repeats):
                factor = factor * (10 ** block_len) + 1

            for x in range(lo, hi + 1):
                invalid.add(x * factor)

    return sorted(invalid)


# ------------------------------------------------------------
# Build prefix sums for fast range summation
# ------------------------------------------------------------
def build_prefix(vals: list[int]) -> list[int]:
    prefix = [0]
    s = 0
    for v in vals:
        s += v
        prefix.append(s)
    return prefix


# ------------------------------------------------------------
# Sum values in [a, b] using binary search
# ------------------------------------------------------------
def sum_in_range(vals: list[int], prefix: list[int], a: int, b: int) -> int:
    l = bisect_left(vals, a)
    r = bisect_right(vals, b)
    return prefix[r] - prefix[l]


# ------------------------------------------------------------
# Solve full input: "a-b,c-d,..."
# ------------------------------------------------------------
def solve(input_line: str) -> int:
    ranges = []
    max_b = 0

    for part in input_line.strip().split(","):
        a_s, b_s = part.split("-")
        a = int(a_s)
        b = int(b_s)
        ranges.append((a, b))
        max_b = max(max_b, b)

    max_digits = len(str(max_b))

    invalid_ids = generate_invalid_ids(max_digits)
    prefix = build_prefix(invalid_ids)

    total = 0
    for a, b in ranges:
        total += sum_in_range(invalid_ids, prefix, a, b)

    return total


# --------------------
# TESTS (Test with small ranges)
# --------------------
# print("Test 1-120 (expected 606):", solve("1-120"))
# print("Test 90-115 (expected 210):", solve("90-115"))

# example = (
#     "11-22,95-115,998-1012,1188511880-1188511890,"
#     "222220-222224,1698522-1698528,446443-446449,"
#     "38593856-38593862,565653-565659,"
#     "824824821-824824827,2121212118-2121212124"
# )
# print("Example (expected 4174379265):", solve(example))


# --------------------
# REAL INPUT
# --------------------
real_input = (
    "69810572-69955342,3434061167-3434167492,76756725-76781020,49-147,296131-386620,910523-946587,34308309-34358652,64542-127485,640436-659023,25-45,35313993-35393518,753722181-753795479,1544-9792,256-647,444628-483065,5863911-6054673,6969623908-6969778569,658-1220,12631-63767,670238-830345,1-18,214165106-214245544,3309229-3355697")

print("♡ FINAL ANSWER: ♡ ", solve(real_input))
