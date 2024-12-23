def solve():
    with open("day_17.txt", "r") as f:
        lines = f.readlines()

    registers = {}
    for line in lines:
        if line.startswith("Register A:"):
            registers['A'] = int(line.split(": ")[1])
        elif line.startswith("Register B:"):
            registers['B'] = int(line.split(": ")[1])
        elif line.startswith("Register C:"):
            registers['C'] = int(line.split(": ")[1])
        elif line.startswith("Program:"):
            program = [int(x) for x in line.split(": ")[1].strip().split(",")]
            break

    ip = 0
    output = []

    def get_literal_operand_value(operand):
        return operand

    def get_combo_operand_value(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:
            raise ValueError("Invalid combo operand")

    while 0 <= ip < len(program):
        opcode = program[ip]

        if ip + 1 >= len(program):
            break

        operand = program[ip + 1]

        if opcode == 0:  # adv
            divisor = 2 ** get_combo_operand_value(operand)
            registers['A'] //= divisor
            ip += 2
        elif opcode == 1:  # bxl
            registers['B'] ^= get_literal_operand_value(operand)
            ip += 2
        elif opcode == 2:  # bst
            registers['B'] = get_combo_operand_value(operand) % 8
            ip += 2
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                ip = get_literal_operand_value(operand)
            else:
                ip += 2
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
            ip += 2
        elif opcode == 5:  # out
            output_value = get_combo_operand_value(operand) % 8
            output.append(str(output_value))
            ip += 2
        elif opcode == 6:  # bdv
            divisor = 2 ** get_combo_operand_value(operand)
            registers['B'] //= divisor
            ip += 2
        elif opcode == 7:  # cdv
            divisor = 2 ** get_combo_operand_value(operand)
            registers['C'] //= divisor
            ip += 2
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    return ",".join(output)

result = solve()
print(result)