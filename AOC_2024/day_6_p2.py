def solve_part_two(filename: str) -> int:
    """Return how many positions can host a new obstacle that traps the guard in a patrol loop."""

    grid = []
    with open(filename, 'r') as f:
        for line in f:
            grid.append(list(line.rstrip('\n')))

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Identify guard’s starting state
    start_r = start_c = None
    dir_index = None
    # Directions in clockwise order: up(0), right(1), down(2), left(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in '^v<>':
                start_r, start_c = r, c
                if grid[r][c] == '^':
                    dir_index = 0
                elif grid[r][c] == '>':
                    dir_index = 1
                elif grid[r][c] == 'v':
                    dir_index = 2
                elif grid[r][c] == '<':
                    dir_index = 3
                # Replace with '.' so it's treated like floor during simulation
                grid[r][c] = '.'
                break
        if start_r is not None:
            break

    def guard_in_loop_with_obstruction() -> bool:
        """Run the guard’s patrol until it either leaves the map or repeats a state."""
        # Start from the known initial state
        gr, gc, d_idx = start_r, start_c, dir_index
        visited_states = set()
        visited_states.add((gr, gc, d_idx))

        while True:
            drow, dcol = directions[d_idx]
            front_r, front_c = gr + drow, gc + dcol

            # (a) If next step is off the grid => guard escapes => no loop
            if not (0 <= front_r < rows and 0 <= front_c < cols):
                return False

            # (b) If next step is an obstacle => turn right
            if grid[front_r][front_c] == '#':
                d_idx = (d_idx + 1) % 4
            else:
                # (c) Otherwise, move forward
                gr, gc = front_r, front_c

            # Check if seen (position + direction) before
            if (gr, gc, d_idx) in visited_states:
                # We found a loop
                return True
            visited_states.add((gr, gc, d_idx))


    valid_placements = 0
    for r in range(rows):
        for c in range(cols):
            # Skip non-floor cells and the guard’s starting cell
            if (r, c) == (start_r, start_c):
                continue
            if grid[r][c] != '.':
                continue

            # Temporarily place an obstacle
            grid[r][c] = '#'
            in_loop = guard_in_loop_with_obstruction()
            # Remove the temporary obstacle
            grid[r][c] = '.'

            if in_loop:
                valid_placements += 1

    return valid_placements


if __name__ == "__main__":
    answer = solve_part_two("day_6.txt")
    print(f"Number of positions that would trap the guard in a loop: {answer}")
