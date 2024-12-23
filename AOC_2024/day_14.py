import re

def solve():
    robots = []
    with open("day_14.txt") as f:
        for line in f:
            match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append({'px': px, 'py': py, 'vx': vx, 'vy': vy})

    width = 101
    height = 103
    time = 100

    final_positions = []
    for robot in robots:
        final_x = (robot['px'] + robot['vx'] * time) % width
        final_y = (robot['py'] + robot['vy'] * time) % height
        final_positions.append((final_x, final_y))

    quadrant_counts = [0, 0, 0, 0]

    center_x = width / 2
    center_y = height / 2

    for x, y in final_positions:
        if x < center_x and y < center_y:
            quadrant_counts[0] += 1
        elif x > center_x and y < center_y:
            quadrant_counts[1] += 1
        elif x < center_x and y > center_y:
            quadrant_counts[2] += 1
        elif x > center_x and y > center_y:
            quadrant_counts[3] += 1

    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count

    return safety_factor

def solve_corrected_quadrant():
    robots = []
    with open("day_14.txt") as f:
        for line in f:
            match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append({'px': px, 'py': py, 'vx': vx, 'vy': vy})

    width = 101
    height = 103
    time = 100

    final_positions = []
    for robot in robots:
        final_x = (robot['px'] + robot['vx'] * time) % width
        final_y = (robot['py'] + robot['vy'] * time) % height
        final_positions.append((final_x, final_y))

    quadrant_counts = [0, 0, 0, 0]

    center_x = width // 2
    center_y = height // 2

    for x, y in final_positions:
        if x < center_x and y < center_y:
            quadrant_counts[0] += 1
        elif x > center_x and y < center_y:
            quadrant_counts[1] += 1
        elif x < center_x and y > center_y:
            quadrant_counts[2] += 1
        elif x > center_x and y > center_y:
            quadrant_counts[3] += 1

    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count

    return safety_factor

result_corrected = solve_corrected_quadrant()
print(result_corrected)