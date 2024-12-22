import re

def solve_part2():
    total_sum = 0
    enabled = True  # mul instructions are initially enabled
    try:
        with open("day_3.txt", "r") as file:
            corrupted_memory = file.read()

        while corrupted_memory:
            mul_match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", corrupted_memory)
            do_match = re.match(r"do\(\)", corrupted_memory)
            dont_match = re.match(r"don't\(\)", corrupted_memory)

            if mul_match:
                if enabled:
                    num1 = int(mul_match.group(1))
                    num2 = int(mul_match.group(2))
                    total_sum += num1 * num2
                corrupted_memory = corrupted_memory[mul_match.end():]
            elif do_match:
                enabled = True
                corrupted_memory = corrupted_memory[do_match.end():]
            elif dont_match:
                enabled = False
                corrupted_memory = corrupted_memory[dont_match.end():]
            else:
                # If no valid instruction is found at the beginning, remove the first character
                corrupted_memory = corrupted_memory[1:]

    except FileNotFoundError:
        print("Error: day_3.txt not found.")
        return

    print(f"The sum of the results of the enabled multiplications is: {total_sum}")

if __name__ == "__main__":
    solve_part2()