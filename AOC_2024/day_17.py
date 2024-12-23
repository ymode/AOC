def solve():
    registers = {'A': 30886132, 'B': 0, 'C': 0}
    program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 4, 5, 5, 3, 0]

    ip = 0
    output = []

    def get_literal_operand_value(operand):
        return operand

    def get_combo_operand_value(operand, registers):
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
            divisor = 2 ** get_combo_operand_value(operand, registers)
            registers['A'] //= divisor
            ip += 2
        elif opcode == 1:  # bxl
            registers['B'] ^= get_literal_operand_value(operand)
            ip += 2
        elif opcode == 2:  # bst
            registers['B'] = get_combo_operand_value(operand, registers) % 8
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
            output_value = get_combo_operand_value(operand, registers) % 8
            output.append(str(output_value))
            ip += 2
        elif opcode == 6:  # bdv
            divisor = 2 ** get_combo_operand_value(operand, registers)
            registers['B'] //= divisor
            ip += 2
        elif opcode == 7:  # cdv
            divisor = 2 ** get_combo_operand_value(operand, registers)
            registers['C'] //= divisor
            ip += 2
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    return ",".join(output)

result = solve()
print(result)