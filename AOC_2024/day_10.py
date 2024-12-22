def solve():
    with open("day_10.txt") as f:
        heightmap = [[int(digit) for digit in line.strip()] for line in f]

    rows = len(heightmap)
    cols = len(heightmap[0])

    trailheads = []
    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] == 0:
                trailheads.append((r, c))

    total_score = 0
    for start_row, start_col in trailheads:
        reachable_nines = set()
        queue = [(start_row, start_col)]
        visited = set([(start_row, start_col)])

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        q = [(start_row, start_col)]
        reachable_height_9_from_this = set()
        q = [(start_row, start_col, 0)]  # row, col, expected_next_height
        visited_states = set([(start_row, start_col)])

        while q:
            r, c, current_height = q.pop(0)

            if heightmap[r][c] == 9:
                reachable_height_9_from_this.add((r, c))
                continue

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and heightmap[nr][nc] == current_height + 1:
                    if (nr, nc) not in visited_states:
                        visited_states.add((nr, nc))
                        q.append((nr, nc, current_height + 1))

        total_score += len(reachable_height_9_from_this)

    return total_score

print(solve())