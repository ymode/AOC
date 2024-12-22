from collections import deque

def solve():
    with open("day_12.txt", "r") as file:
        grid = [line.strip() for line in file]

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                region_cells = set()
                queue = deque([(r, c)])
                visited[r][c] = True

                while queue:
                    row, col = queue.popleft()
                    region_cells.add((row, col))

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and \
                           not visited[nr][nc] and grid[nr][nc] == plant_type:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

                regions.append((plant_type, region_cells))

    total_price = 0
    for plant_type, region_cells in regions:
        area = len(region_cells)
        perimeter = 0
        for r, c in region_cells:
            # Check neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) in region_cells):
                    perimeter += 1

        price = area * perimeter
        total_price += price

    return total_price

result = solve()
print(result)