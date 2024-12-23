def solve():
    with open("day_15.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Separate the map lines from the moves
    warehouse_map = []
    moves_list = []
    reading_map = True

    for line in lines:
        # If still reading map lines, look for '#'
        if reading_map:
            if '#' in line:
                warehouse_map.append(line)
            else:
                # Reached a line without '#'; switch to reading moves
                reading_map = False
                moves_list.append(line.strip())
        else:
            moves_list.append(line.strip())

    # Join all lines of moves into one giant moves string
    moves_str = "".join(moves_list)

    # Convert the map to a list of strings or keep as is
    rows = len(warehouse_map)
    cols = len(warehouse_map[0]) if rows > 0 else 0

    # Locate the robot and boxes
    robot_r = robot_c = None
    boxes = set()

    for r in range(rows):
        for c in range(cols):
            ch = warehouse_map[r][c]
            if ch == '@':
                robot_r, robot_c = r, c
            elif ch == 'O':
                boxes.add((r, c))

    # Helper to get row/col deltas
    def move_delta(m):
        if m == '^':
            return -1, 0
        elif m == 'v':
            return 1, 0
        elif m == '<':
            return 0, -1
        elif m == '>':
            return 0, 1
        return 0, 0

    # Check for a wall
    def is_wall(rr, cc):
        return warehouse_map[rr][cc] == '#'

    def in_bounds(rr, cc):
        return 0 <= rr < rows and 0 <= cc < cols

    def can_push_chain(start_r, start_c, dr, dc):
        
        chain_positions = []
        rr, cc = start_r, start_c

        # 1) Gather consecutive boxes in a line
        while (rr, cc) in boxes:
            chain_positions.append((rr, cc))
            rr += dr
            cc += dc

        if not in_bounds(rr, cc):
            return (False, [])
        if is_wall(rr, cc):
            return (False, [])
        if (rr, cc) in boxes:
          
            return (False, [])

        new_positions = []
        for old_r, old_c in reversed(chain_positions):
            new_positions.append((old_r + dr, old_c + dc))

        
        new_positions.reverse()
        return (True, new_positions)

   
    for m in moves_str:
        dr, dc = move_delta(m)
        next_r = robot_r + dr
        next_c = robot_c + dc

        if not in_bounds(next_r, next_c):
            continue
        if is_wall(next_r, next_c):
            continue

        if (next_r, next_c) not in boxes:
            robot_r, robot_c = next_r, next_c
        else:
           
            can_push, new_chain_positions = can_push_chain(next_r, next_c, dr, dc)
            if can_push:
               
                chain = []
                rr, cc = next_r, next_c
                while (rr, cc) in boxes:
                    chain.append((rr, cc))
                    rr += dr
                    cc += dc

                for old_b in chain:
                    boxes.remove(old_b)
                for np in new_chain_positions:
                    boxes.add(np)

                # Move robot forward
                robot_r, robot_c = next_r, next_c
            else:
                # Robot doesn't move, do nothing
                continue

  
    gps_sum = sum(100 * r + c for (r, c) in boxes)
    return gps_sum

if __name__ == "__main__":
    result = solve()
    print(result)
