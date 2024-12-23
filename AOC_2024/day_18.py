from collections import deque

def solve():
    grid_size = 71
    start = (0, 0)
    end = (70, 70)

    with open("day_18.txt") as f:
        byte_positions = [line.strip().split(',') for line in f]
        byte_positions = [(int(x), int(y)) for x, y in byte_positions]

    corrupted = set()
    for i in range(min(1024, len(byte_positions))):
        x, y = byte_positions[i]
        corrupted.add((x, y))

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (current_x, current_y), steps = queue.popleft()

        if (current_x, current_y) == end:
            return steps

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = current_x + dx, current_y + dy

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size and \
               (next_x, next_y) not in corrupted and \
               (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), steps + 1))

    return -1

result = solve()
print(result)