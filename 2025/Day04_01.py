def parse_grid(input_text: str) -> list[list[str]]:
    """
    Reads the puzzle input and returns a 2D grid (matrix) of characters.
    Each row is a list of chars: '.' or '@'
    """
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]

    # Optional safety check: all rows must have the same length
    width = len(lines[0])
    for i, line in enumerate(lines):
        if len(line) != width:
            raise ValueError(f"Row {i} has length {len(line)}, expected {width}. Check line wrapping/copy-paste.")

    grid = [list(line) for line in lines]
    return grid

def solve(input_text: str) -> int:
    grid = parse_grid(input_text)
    rows = len(grid)
    cols = len(grid[0])

    count = 0  # ✅ inicializa

    for r in range(rows):
        for c in range(cols):

            # ✅ só conta se a célula atual é um rolo
            if grid[r][c] != '@':
                continue

            adjacents = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc] == '@':
                        adjacents += 1

            if adjacents < 4:
                count += 1

    return count


# --------------------
# Example input (small)
# --------------------
example_input = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


print("Example answer with test input. Eexpected answer 13: ", solve(example_input))



with open("input_day04.txt", "r") as f:
    input_text = f.read()

grid = parse_grid(input_text)
rows = len(grid)
cols = len(grid[0])
print("\n\nRows:", rows, "Cols:", cols)

print("Final Answer Day 4 - Part 1 - (｡♥‿♥｡):", solve(input_text))


