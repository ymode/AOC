def evaluate_part2(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        op = operators[i]
        num = numbers[i + 1]
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))
    return result

def solve_part2():
    total_calibration_result = 0
    with open("day_7.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(":")
            target = int(parts[0])
            numbers = [int(x) for x in parts[1].strip().split()]

            if len(numbers) == 1:
                if numbers[0] == target:
                    total_calibration_result += target
                continue

            num_operators = len(numbers) - 1
            is_equation_true = False

            for i in range(3**num_operators):
                operators = []
                temp = i
                for _ in range(num_operators):
                    remainder = temp % 3
                    if remainder == 0:
                        operators.insert(0, '+')
                    elif remainder == 1:
                        operators.insert(0, '*')
                    elif remainder == 2:
                        operators.insert(0, '||')
                    temp //= 3

                result = evaluate_part2(numbers, operators)
                if result == target:
                    is_equation_true = True
                    break

            if is_equation_true:
                total_calibration_result += target

    return total_calibration_result

if __name__ == "__main__":
    result = solve_part2()
    print(result)