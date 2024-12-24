#!/usr/bin/env python3

import collections

def read_input(filename):
    with open(filename) as f:
        grid = [line.rstrip('\n') for line in f]
    R = len(grid)
    C = len(grid[0])

    start = None
    end = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    return grid, R, C, start, end

def neighbors(r, c, R, C):
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc

def is_track(cell, grid):
    r, c = cell
    return grid[r][c] in ('.', 'S', 'E')

def bfs_from_cell(start_cell, grid, R, C):
    from collections import deque

    dist_map = {}
    visited = set()
    visited.add(start_cell)
    dist_map[start_cell] = 0

    queue = deque([start_cell])
    while queue:
        cr, cc = queue.popleft()
        for nr, nc in neighbors(cr, cc, R, C):
            if (nr, nc) not in visited and is_track((nr, nc), grid):
                visited.add((nr, nc))
                dist_map[(nr, nc)] = dist_map[(cr, cc)] + 1
                queue.append((nr, nc))
    return dist_map

def ignoring_walls_reachable_in_1_or_2_steps(cell, R, C, grid):
    """
    Return { reachable_cell: steps_used } for up to 2 ignoring-wall steps.
    ignoring-wall steps means we do NOT check is_track for intermediate squares,
    but the final square must be track.
    """
    from collections import deque
    
    r0, c0 = cell
    visited = {(r0,c0): 0}
    queue = deque([(r0,c0,0)])
    results = {}

    while queue:
        r, c, steps_used = queue.popleft()
        if 0 < steps_used <= 2:
            # If the final position is track, record it.
            if is_track((r,c), grid):
                # keep the smaller steps if multiple ways
                if (r,c) not in results:
                    results[(r,c)] = steps_used
                else:
                    results[(r,c)] = min(results[(r,c)], steps_used)

        if steps_used < 2:
            # expand further
            for nr, nc in neighbors(r, c, R, C):
                # ignoring walls => do not check if grid[nr][nc] is '#'
                nxt = visited.get((nr,nc), 9999)
                if steps_used + 1 < nxt:
                    visited[(nr,nc)] = steps_used + 1
                    queue.append((nr,nc, steps_used + 1))
    
    # we do NOT want to include the cell itself with 0 steps
    if cell in results:
        del results[cell]
    return results

def solve(filename="day_20.txt"):
    grid, R, C, start, end = read_input(filename)

    # BFS from S
    distS = bfs_from_cell(start, grid, R, C)
    if end not in distS:
        print("No normal path from S to E. So no cheats can help.")
        return
    
    # BFS from E (to quickly get dist for B->E)
    distE = bfs_from_cell(end, grid, R, C)

    # BFS from every track cell to get distances all_distances[A][B]
    # (If the grid is small enough to handle that approach.)
    all_distances = {}
    track_cells = []
    for r in range(R):
        for c in range(C):
            if is_track((r,c), grid):
                track_cells.append((r,c))
    for cell in track_cells:
        all_distances[cell] = bfs_from_cell(cell, grid, R, C)

    big_saving_cheats = 0

    # For each A, see which B’s are reachable via ignoring-walls steps
    for A in track_cells:
        # Must be reachable from S in normal mode
        if A not in distS:
            continue
        ignoring_map = ignoring_walls_reachable_in_1_or_2_steps(A, R, C, grid)
        
        for B, steps_used in ignoring_map.items():
            # B must be reachable from E in normal mode
            if B not in distE:
                continue
            # Must have normal BFS distance A->B
            if B not in all_distances[A]:
                continue

            normal_dist_AB = all_distances[A][B]
            # Overall route with cheat: S->A (distS[A]) + cheat A->B (steps_used) + B->E (distE[B])
            cheat_route_len = distS[A] + steps_used + distE[B]
            # Normal route if you walk S->A->B->E in normal BFS:
            normal_route_len = distS[A] + normal_dist_AB + distE[B]

            # The difference is the actual saving from S to E
            time_saved = normal_route_len - cheat_route_len
            if time_saved >= 100:
                big_saving_cheats += 1

    print("Number of cheats saving >= 100 picoseconds:", big_saving_cheats)

if __name__ == "__main__":
    solve()
