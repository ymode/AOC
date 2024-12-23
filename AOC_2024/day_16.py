import heapq

def solve():
    with open("day_16.txt", "r") as f:
        grid = [line.strip() for line in f]

    rows = len(grid)
    cols = len(grid[0])

    start_row, start_col = -1, -1
    end_row, end_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
            elif grid[r][c] == 'E':
                end_row, end_col = r, c

    direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E, S, W, N

    scores = {}
    pq = [(0, start_row, start_col, 0)]  # (score, row, col, direction)
    scores[(start_row, start_col, 0)] = 0

    while pq:
        current_score, row, col, direction = heapq.heappop(pq)

        if current_score > scores.get((row, col, direction), float('inf')):
            continue

        if row == end_row and col == end_col:
            return current_score

        # Move forward
        dr, dc = direction_vectors[direction]
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
            new_score = current_score + 1
            if new_score < scores.get((new_row, new_col, direction), float('inf')):
                scores[(new_row, new_col, direction)] = new_score
                heapq.heappush(pq, (new_score, new_row, new_col, direction))

        # Rotate clockwise
        new_direction = (direction + 1) % 4
        new_score = current_score + 1000
        if new_score < scores.get((row, col, new_direction), float('inf')):
            scores[(row, col, new_direction)] = new_score
            heapq.heappush(pq, (new_score, row, col, new_direction))

        # Rotate counterclockwise
        new_direction = (direction - 1 + 4) % 4
        new_score = current_score + 1000
        if new_score < scores.get((row, col, new_direction), float('inf')):
            scores[(row, col, new_direction)] = new_score
            heapq.heappush(pq, (new_score, row, col, new_direction))

    return -1

result = solve()
print(result)