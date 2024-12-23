from collections import deque

def is_reachable(grid_size, start, end, corrupted):
    queue = deque([start])
    visited = {start}

    while queue:
        current_x, current_y = queue.popleft()

        if (current_x, current_y) == end:
            return True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = current_x + dx, current_y + dy

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size and \
               (next_x, next_y) not in corrupted and \
               (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))
    return False

def solve_part2():
    grid_size = 71
    start = (0, 0)
    end = (70, 70)

    with open("day_18.txt") as f:
        byte_positions = [line.strip().split(',') for line in f]
        byte_positions = [(int(x), int(y)) for x, y in byte_positions]

    corrupted = set()
    for i, (bx, by) in enumerate(byte_positions):
        if not is_reachable(grid_size, start, end, corrupted):
            return f"{byte_positions[i-1][0]},{byte_positions[i-1][1]}"

        corrupted.add((bx, by))

    return "Solution not found"

result_part2 = solve_part2()
print(result_part2)