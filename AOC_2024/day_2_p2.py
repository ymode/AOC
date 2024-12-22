def is_safe_original(report):
    """Checks if a report is safe according to the original rules."""
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

def is_safe_with_dampener(report):
    """Checks if a report is safe, considering the Problem Dampener."""
    if is_safe_original(report):
        return True

    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if is_safe_original(temp_report):
            return True

    return False

def solve_part2():
    safe_reports_count = 0
    try:
        with open("day_2.txt", "r") as file:
            for line in file:
                levels_str = line.strip().split()
                if levels_str:
                    levels = [int(level) for level in levels_str]
                    if is_safe_with_dampener(levels):
                        safe_reports_count += 1
    except FileNotFoundError:
        print("Error: day_2.txt not found.")
        return

    print(f"Number of safe reports (with Problem Dampener): {safe_reports_count}")

if __name__ == "__main__":
    solve_part2()