def solve_guard_path(filename: str) -> int:
    """Simulate the guard's path and return how many distinct positions are visited."""
    grid = []
    
    with open(filename, 'r') as f:
        for line in f:
            grid.append(list(line.rstrip('\n')))
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position & direction
    guard_r = guard_c = None
    direction = None  # will be one of 'up', 'down', 'left', 'right'
    
    # Directions in clockwise order: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in '^v<>':
                guard_r, guard_c = r, c
                if grid[r][c] == '^':
                    dir_index = 0  # 'up'
                elif grid[r][c] == '>':
                    dir_index = 1  # 'right'
                elif grid[r][c] == 'v':
                    dir_index = 2  # 'down'
                elif grid[r][c] == '<':
                    dir_index = 3  # 'left'
                # Remove the symbol, treat it like floor 
                grid[r][c] = '.'
                break
        if guard_r is not None:
            break

    visited = set()
    visited.add((guard_r, guard_c))


    while True:
        drow, dcol = directions[dir_index]
        front_r = guard_r + drow
        front_c = guard_c + dcol

        
        if not (0 <= front_r < rows and 0 <= front_c < cols):
            break

      
        if grid[front_r][front_c] == '#':
            dir_index = (dir_index + 1) % 4
            continue

        guard_r, guard_c = front_r, front_c
        visited.add((guard_r, guard_c))

 
    return len(visited)


if __name__ == "__main__":
    answer = solve_guard_path("day_6.txt")
    print(f"Distinct positions visited before leaving the map: {answer}")
