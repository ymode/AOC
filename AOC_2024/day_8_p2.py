def solve_part2():
    with open("day_8.txt", "r") as f:
        grid = [line.strip() for line in f]

    rows = len(grid)
    cols = len(grid[0])

    antennas_by_frequency = {}
    for r in range(rows):
        for c in range(cols):
            freq = grid[r][c]
            if freq != '.':
                if freq not in antennas_by_frequency:
                    antennas_by_frequency[freq] = []
                antennas_by_frequency[freq].append((r, c))

    antinodes = set()

    def is_collinear(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

    for freq, antennas in antennas_by_frequency.items():
        n = len(antennas)
        if n < 2:
            continue

        for i in range(n):
            for j in range(i + 1, n):
                p1 = antennas[i]
                p2 = antennas[j]

                # Add the locations of the two antennas that define the line
                antinodes.add(p1)
                antinodes.add(p2)

                # Iterate through all grid points to find antinodes on the line
                min_r = min(p1[0], p2[0])
                max_r = max(p1[0], p2[0])
                min_c = min(p1[1], p2[1])
                max_c = max(p1[1], p2[1])

                for r in range(rows):
                    for c in range(cols):
                        p3 = (r, c)
                        if is_collinear(p1, p2, p3):
                            antinodes.add(p3)

    return len(antinodes)

if __name__ == "__main__":
    result = solve_part2()
    print(result)