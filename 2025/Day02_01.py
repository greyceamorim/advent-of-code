
print("Oieee! Day 2 - part 1\n\nLet's do this!")
print("\n              meow  ฅ^•ﻌ•^ฅ meow")
print("\nI am using ChatGPT to help me with the logic {•ᴗ•}♡\n\n")
# -----------------------------
# Day 2 - Part 1 (AoC-style)
# Invalid IDs are exactly "XX" (a digit-sequence repeated twice).
#
# Example invalid:
#   55      -> "5" repeated twice
#   6464    -> "64" repeated twice
#   123123  -> "123" repeated twice
#
# We must sum all invalid IDs inside multiple ranges "start-end".
# -----------------------------

def ceil_div(a: int, b: int) -> int:
    """
    Integer ceiling division for positive integers: ceil(a / b)

    Why does this work?
    - Normal integer division (//) truncates down.
    - To round up, we use: (a + b - 1) // b

    Example:
      201 // 100 = 2
      299 // 100 = 2
      300 // 100 = 3

    With ceil_div:
      ceil_div(201, 100) = (201 + 99) // 100 = 300 // 100 = 3
      ceil_div(299, 100) = (299 + 99) // 100 = 398 // 100 = 3
      ceil_div(300, 100) = (300 + 99) // 100 = 399 // 100 = 3
    """
    return (a + b - 1) // b


def sum_invalid_in_range_part1(a: int, b: int) -> int:
    """
    Sum all numbers n in [a, b] that are exactly "XX"
    (a sequence of digits repeated twice).

    If X has k digits, then:
        n = X * (10^k + 1)
    because:
        "XX" = X * 10^k + X = X * (10^k + 1)

    Constraints:
    - X must have exactly k digits -> X in [10^(k-1), 10^k - 1]
    - No leading zeros in IDs, so this is valid.

    Instead of iterating every n in [a,b], we iterate possible k and compute
    the valid X interval via division, then sum using arithmetic series.
    """
    total = 0

    # Your real input has numbers up to ~10 digits, so k up to 5 covers 2k <= 10.
    # If you ever get larger IDs, increase this range accordingly.
    for k in range(1, 6):
        m = 10**k + 1  # factor (10^k + 1)

        # X must be k digits
        x_min_digits = 10**(k - 1)
        x_max_digits = 10**k - 1

        # From a <= X*m <= b:
        #   X >= ceil(a / m)
        #   X <= floor(b / m)
        x_lo = ceil_div(a, m)
        x_hi = b // m

        # Intersect with "X is k digits"
        L = max(x_lo, x_min_digits)
        R = min(x_hi, x_max_digits)

        if L <= R:
            # Sum of X from L..R is arithmetic series:
            # sum_x = (L + R) * count / 2
            count = R - L + 1
            sum_x = (L + R) * count // 2

            # Each invalid number is n = X*m
            total += m * sum_x

    return total


def solve_part1(input_line: str) -> int:
    """
    Parse comma-separated ranges: "a-b,c-d,..."
    Sum invalid IDs over all ranges.
    """
    grand_total = 0
    for part in input_line.strip().split(","):
        start_s, end_s = part.split("-")
        a = int(start_s)
        b = int(end_s)
        grand_total += sum_invalid_in_range_part1(a, b)
    return grand_total


# --------------------
# TESTS (run these first)
# --------------------
# Test A: in range 1..120, invalid "XX" values are:
# 11,22,33,44,55,66,77,88,99 -> sum = 495
print("Test 1-120 (expected 495):", solve_part1("1-120"))

# Test B: in range 1000..1100, only "1010" fits exactly XX -> sum = 1010
print("Test 1000-1100 (expected 1010):", solve_part1("1000-1100"))

# Test C: example from the prompt (Part 1 example sum expected 1227775554)
# example = (
#     "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
#     "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
#     "824824821-824824827,2121212118-2121212124"
# )
# print("Test prompt example (expected 1227775554):", solve_part1(example))


# --------------------
# REAL INPUT (uncomment when tests match)
# --------------------
real_input = (
    "69810572-69955342,3434061167-3434167492,76756725-76781020,49-147,"
    "296131-386620,910523-946587,34308309-34358652,64542-127485,640436-659023,"
    "25-45,35313993-35393518,753722181-753795479,1544-9792,256-647,444628-483065,"
    "5863911-6054673,6969623908-6969778569,658-1220,12631-63767,670238-830345,"
    "1-18,214165106-214245544,3309229-3355697"
)

print("\n\n♡ FINAL ANSWER with Real Input (Part 1): ♡ ", solve_part1(real_input))

