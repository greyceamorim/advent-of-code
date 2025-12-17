from collections import deque


def parse_grid(input_text: str) -> list[list[str]]:
    """
    Reads the puzzle input and returns a 2D grid (matrix) of characters.
    Each row is a list of chars: '.' or '@'
    """
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]

    width = len(lines[0])
    for i, line in enumerate(lines):
        if len(line) != width:
            raise ValueError(
                f"Row {i} has length {len(line)}, expected {width}. "
                "Check line wrapping or copy-paste issues."
            )

    return [list(line) for line in lines]


def solve(input_text: str) -> int:
    grid = parse_grid(input_text)
    rows = len(grid)
    cols = len(grid[0])

    # Stores how many '@' neighbors each cell has
    neighbor_count = [[0] * cols for _ in range(rows)]

    # All 8 directions around a cell
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    # Step 1: compute initial neighbor counts
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        count += 1

            neighbor_count[r][c] = count

    # Step 2: queue all initially accessible rolls (< 4 neighbors)
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and neighbor_count[r][c] < 4:
                queue.append((r, c))

    removed = 0

    # Step 3: iterative removal (BFS-style)
    while queue:
        r, c = queue.popleft()

        # Might have been removed already
        if grid[r][c] != '@':
            continue

        # Remove this roll
        grid[r][c] = '.'
        removed += 1

        # Update neighbors
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    neighbor_count[nr][nc] -= 1

                    # If it just became accessible, add to queue
                    if neighbor_count[nr][nc] == 3:
                        queue.append((nr, nc))

    return removed


# --------------------
# Run with real input
# --------------------
with open("input_day04.txt", "r") as f:
    input_text = f.read()


print("Final Answer Day 4 - Part 2 -(￣▽￣)ゞ:", solve(input_text))


