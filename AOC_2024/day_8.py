def solve():
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

    for freq, antennas in antennas_by_frequency.items():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                r1, c1 = antennas[i]
                r2, c2 = antennas[j]

                def is_within_bounds(r, c):
                    return 0 <= r < rows and 0 <= c < cols

                # Potential antinodes
                # Case 1: P1 is closer
                ar1 = 2 * r1 - r2
                ac1 = 2 * c1 - c2
                if is_within_bounds(ar1, ac1):
                    antinodes.add((ar1, ac1))

                # Case 2: P2 is closer
                ar2 = 2 * r2 - r1
                ac2 = 2 * c2 - c1
                if is_within_bounds(ar2, ac2):
                    antinodes.add((ar2, ac2))

                # Case 3: Antinode between, closer to P1
                if (2 * r1 + r2) % 3 == 0 and (2 * c1 + c2) % 3 == 0:
                    ar3 = (2 * r1 + r2) // 3
                    ac3 = (2 * c1 + c2) // 3
                    if is_within_bounds(ar3, ac3):
                        antinodes.add((ar3, ac3))

                # Case 4: Antinode between, closer to P2
                if (r1 + 2 * r2) % 3 == 0 and (c1 + 2 * c2) % 3 == 0:
                    ar4 = (r1 + 2 * r2) // 3
                    ac4 = (c1 + 2 * c2) // 3
                    if is_within_bounds(ar4, ac4):
                        antinodes.add((ar4, ac4))

    return len(antinodes)

if __name__ == "__main__":
    result = solve()
    print(result)