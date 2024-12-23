import re

def solve_part2_easter_egg(filename="day_14.txt", max_time=10000):
    
    robots = []
    with open(filename, "r") as f:
        for line in f:
            match = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line.strip())
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append((px, py, vx, vy))

    width, height = 101, 103


    min_area = float("inf")
    best_time = 0
 
    all_positions = []

    for t in range(max_time):
        # Calculate positions at time t
        current_positions = []
        for (px, py, vx, vy) in robots:
            x_t = (px + vx * t) % width
            y_t = (py + vy * t) % height
            current_positions.append((x_t, y_t))

        all_positions.append(current_positions)

        # Compute bounding box 
        xs = [p[0] for p in current_positions]
        ys = [p[1] for p in current_positions]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        box_w = (maxx - minx) + 1
        box_h = (maxy - miny) + 1
        area = box_w * box_h

       
        if area < min_area:
            min_area = area
            best_time = t

    
    print(f"Smallest bounding box occurs at t = {best_time}, area = {min_area}")

    # Retrieve the positions for best_time
    best_positions = all_positions[best_time]

    # Build and print the ASCII arrangement for best_time
    xs = [p[0] for p in best_positions]
    ys = [p[1] for p in best_positions]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    box_w = maxx - minx + 1
    box_h = maxy - miny + 1

    # Create 2D grid for visualization
    grid = [["." for _ in range(box_w)] for _ in range(box_h)]
    for (x, y) in best_positions:
        grid[y - miny][x - minx] = "#"

    print(f"\nArrangement at t = {best_time}:")
    for row in grid:
        print("".join(row))

    return best_time  


if __name__ == "__main__":
    solve_part2_easter_egg("day_14.txt", max_time=10000)
