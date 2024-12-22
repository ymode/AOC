def is_safe(report):
    """Checks if a report is safe according to the given rules."""
    if len(report) <= 1:
        return True  # A single level report is considered safe

    # Check if all increasing or all decreasing
    is_increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))

    if not is_increasing and not is_decreasing:
        return False

    # Check adjacent differences
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i+1])
        if not (1 <= diff <= 3):
            return False

    return True

def solve():
    safe_reports_count = 0
    try:
        with open("day_2.txt", "r") as file:
            for line in file:
                levels_str = line.strip().split()
                if levels_str:
                    levels = [int(level) for level in levels_str]
                    if is_safe(levels):
                        safe_reports_count += 1
    except FileNotFoundError:
        print("Error: day_2.txt not found.")
        return

    print(f"Number of safe reports: {safe_reports_count}")

if __name__ == "__main__":
    solve()