from collections import deque

def solve():
    numeric_keypad_layout = {
        (0, 0): '7', (0, 1): '8', (0, 2): '9',
        (1, 0): '4', (1, 1): '5', (1, 2): '6',
        (2, 0): '1', (2, 1): '2', (2, 2): '3',
        (3, 1): '0', (3, 2): 'A',
    }
    numeric_keypad_positions = {v: k for k, v in numeric_keypad_layout.items()}

    directional_keypad_layout = {
        (0, 1): '^', (0, 2): 'A',
        (1, 0): '<', (1, 1): 'v', (1, 2): '>',
    }
    directional_keypad_positions = {v: k for k, v in directional_keypad_layout.items()}

    codes = ["140A", "143A", "349A", "582A", "964A"]
    total_complexity = 0

    for code_to_type in codes:
        target_numeric_sequence = list(code_to_type)

        def is_valid_numeric_pos(pos):
            return pos in numeric_keypad_layout

        def get_numeric_move(current_pos, move):
            r, c = current_pos
            if move == '^': return (r - 1, c)
            elif move == 'v': return (r + 1, c)
            elif move == '<': return (r, c - 1)
            elif move == '>': return (r, c + 1)
            return None

        def is_valid_directional_pos(pos):
            return pos in directional_keypad_layout

        def get_directional_move(current_pos, move):
            r, c = current_pos
            if move == '^': return (r - 1, c)
            elif move == 'v': return (r + 1, c)
            elif move == '<': return (r, c - 1)
            elif move == '>': return (r, c + 1)
            return None

        start_your_pos = directional_keypad_positions['A']
        start_robot2_pos = directional_keypad_positions['A']
        start_robot1_pos = numeric_keypad_positions['A']

        queue = deque([((start_your_pos, start_robot2_pos, start_robot1_pos, 0), [])])
        visited = {((start_your_pos, start_robot2_pos, start_robot1_pos, 0))}
        shortest_your_sequence = None

        while queue:
            (current_your_pos, current_robot2_pos, current_robot1_pos, typed_count), your_sequence = queue.popleft()

            if typed_count == len(target_numeric_sequence):
                shortest_your_sequence = your_sequence
                break

            # Possible actions on your keypad
            for your_action_key, your_action_val in directional_keypad_layout.items():
                new_your_pos = current_your_pos
                if your_action_val != 'A': # Movement on your keypad
                    move_dr, move_dc = 0, 0
                    if your_action_val == '^': move_dr = -1
                    elif your_action_val == 'v': move_dr = 1
                    elif your_action_val == '<': move_dc = -1
                    elif your_action_val == '>': move_dc = 1

                    potential_new_your_pos = (current_your_pos[0] + move_dr, current_your_pos[1] + move_dc)
                    if is_valid_directional_pos(potential_new_your_pos):
                        new_your_pos = potential_new_your_pos

                    new_state = (new_your_pos, current_robot2_pos, current_robot1_pos, typed_count)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, your_sequence + [your_action_val]))
                elif your_action_val == 'A': # Your 'A' press
                    robot2_action = directional_keypad_layout.get(current_your_pos)
                    if robot2_action:
                        new_robot2_pos = current_robot2_pos
                        if robot2_action != 'A':
                            move_dr, move_dc = 0, 0
                            if robot2_action == '^': move_dr = -1
                            elif robot2_action == 'v': move_dr = 1
                            elif robot2_action == '<': move_dc = -1
                            elif robot2_action == '>': move_dc = 1
                            potential_new_robot2_pos = (current_robot2_pos[0] + move_dr, current_robot2_pos[1] + move_dc)
                            if is_valid_directional_pos(potential_new_robot2_pos):
                                new_robot2_pos = potential_new_robot2_pos

                            new_state = (current_your_pos, new_robot2_pos, current_robot1_pos, typed_count)
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, your_sequence + ['A']))

                        elif robot2_action == 'A':
                            robot1_action = directional_keypad_layout.get(current_robot2_pos)
                            if robot1_action:
                                new_robot1_pos = current_robot1_pos
                                if robot1_action != 'A':
                                    potential_new_robot1_pos = get_numeric_move(current_robot1_pos, robot1_action)
                                    if is_valid_numeric_pos(potential_new_robot1_pos):
                                        new_robot1_pos = potential_new_robot1_pos
                                    new_state = (current_your_pos, current_robot2_pos, new_robot1_pos, typed_count)
                                    if new_state not in visited:
                                        visited.add(new_state)
                                        queue.append((new_state, your_sequence + ['A']))
                                elif robot1_action == 'A' and typed_count < len(target_numeric_sequence) and numeric_keypad_layout.get(current_robot1_pos) == target_numeric_sequence[typed_count]:
                                    new_typed_count = typed_count + 1
                                    new_state = (current_your_pos, current_robot2_pos, current_robot1_pos, new_typed_count)
                                    if new_state not in visited:
                                        visited.add(new_state)
                                        queue.append((new_state, your_sequence + ['A']))

        if shortest_your_sequence:
            numeric_part = int(code_to_type[:-1]) if code_to_type[:-1] else 0
            complexity = len(shortest_your_sequence) * numeric_part
            total_complexity += complexity
            print(f"Shortest sequence length for {code_to_type}: {len(shortest_your_sequence)}, Complexity: {complexity}")
        else:
            print(f"Could not find sequence for {code_to_type}")
            return

    print(f"Total complexity: {total_complexity}")

solve()
