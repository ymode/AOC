import re

def solve_part1():
    total_sum = 0
    try:
        with open("day_3.txt", "r") as file:
            corrupted_memory = file.read()

        # Regex to find valid mul instructions
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", corrupted_memory)

        for match in matches:
            num1 = int(match[0])
            num2 = int(match[1])
            total_sum += num1 * num2

    except FileNotFoundError:
        print("Error: day_3.txt not found.")
        return

    print(f"The sum of the results of the multiplications is: {total_sum}")

if __name__ == "__main__":
    solve_part1()