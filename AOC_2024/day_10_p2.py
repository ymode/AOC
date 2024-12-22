def solve_part_two():
    with open("day_10.txt") as f:
        heightmap = [[int(digit) for digit in line.strip()] for line in f]

    rows = len(heightmap)
    cols = len(heightmap[0])

    trailheads = []
    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] == 0:
                trailheads.append((r, c))

    total_rating_sum = 0

    for start_row, start_col in trailheads:
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[start_row][start_col] = 1

        for h in range(1, 10):
            for r in range(rows):
                for c in range(cols):
                    if heightmap[r][c] == h:
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            prev_r, prev_c = r + dr, c + dc
                            if 0 <= prev_r < rows and 0 <= prev_c < cols and heightmap[prev_r][prev_c] == h - 1:
                                dp[r][c] += dp[prev_r][prev_c]

        trailhead_rating = 0
        for r in range(rows):
            for c in range(cols):
                if heightmap[r][c] == 9:
                    trailhead_rating += dp[r][c]

        total_rating_sum += trailhead_rating

    return total_rating_sum

print(solve_part_two())