import re

def solve_machine(ax, ay, bx, by, tx, ty):
    min_cost = float('inf')
    for num_a in range(101):
        if bx != 0:
            if (tx - num_a * ax) % bx == 0:
                num_b_x = (tx - num_a * ax) // bx
                if 0 <= num_b_x <= 100:
                    if ay * num_a + by * num_b_x == ty:
                        cost = num_a * 3 + num_b_x
                        min_cost = min(min_cost, cost)
        elif tx == num_a * ax:
            if by != 0:
                if (ty - num_a * ay) % by == 0:
                    num_b = (ty - num_a * ay) // by
                    if 0 <= num_b <= 100:
                        cost = num_a * 3 + num_b
                        min_cost = min(min_cost, cost)
            elif ty == num_a * ay:
                cost = num_a * 3
                min_cost = min(min_cost, cost)
    return min_cost if min_cost != float('inf') else None

def solve():
    total_cost = 0
    with open("day_13.txt", "r") as file:
        while True:
            line1 = file.readline().strip()
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            blank_line = file.readline().strip()  # Read the blank line

            if not line1:  # End of file
                break

            if not line1.startswith("Button A:"):
                print(f"Skipping unexpected line: {line1}")
                continue
            if not line2.startswith("Button B:"):
                print(f"Skipping unexpected line: {line2}")
                continue
            if not line3.startswith("Prize:"):
                print(f"Skipping unexpected line: {line3}")
                continue

            a_vals = re.findall(r"([-+]?\d+)", line1)
            ax = int(a_vals[0])
            ay = int(a_vals[1])

            b_vals = re.findall(r"([-+]?\d+)", line2)
            bx = int(b_vals[0])
            by = int(b_vals[1])

            prize_part = line3.split(": ")[1]
            tx = int(prize_part.split(", ")[0].split("=")[1])
            ty = int(prize_part.split(", ")[1].split("=")[1])

            min_cost = solve_machine(ax, ay, bx, by, tx, ty)
            if min_cost is not None:
                total_cost += min_cost
    return total_cost

if __name__ == "__main__":
    result = solve()
    print(result)