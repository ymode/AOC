import re

def solve():
    with open("day_24.txt") as f:
        lines = f.read().strip().split("\n")

    wires = {}
    gates = []

    # Parse initial values
    gate_lines = []
    for line in lines:
        if ":" in line and "->" not in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            gate_lines.append(line)

    # Parse gates
    for line in gate_lines:
        match = re.match(r"(.+) -> (.+)", line)
        if match:
            inputs_op, output = match.groups()
            parts = inputs_op.split()
            if len(parts) == 3:
                input1, op, input2 = parts
                gates.append({'input1': input1, 'op': op, 'input2': input2, 'output': output})
            else:
                raise ValueError(f"Unexpected gate format: {line}")

    while True:
        new_wires = {}
        made_update = False

        for gate in list(gates):
            try:
                input1_val = wires.get(gate['input1'])
                input2_val = wires.get(gate['input2'])

                if input1_val is not None and input2_val is not None:
                    if gate['op'] == "AND":
                        output_val = input1_val & input2_val
                    elif gate['op'] == "OR":
                        output_val = input1_val | input2_val
                    elif gate['op'] == "XOR":
                        output_val = input1_val ^ input2_val

                    if gate['output'] not in wires or wires[gate['output']] != output_val:
                        new_wires[gate['output']] = output_val
                        made_update = True
            except KeyError:
                pass  # Input might be a direct value

        if not made_update:
            break

        wires.update(new_wires)

    z_wires = sorted([wire for wire in wires if wire.startswith('z')], key=lambda x: int(x[1:]))
    binary_string = "".join(str(wires[wire]) for wire in z_wires[::-1])  # Reverse for least significant bit
    decimal_output = int(binary_string, 2)

    return decimal_output

print(solve())