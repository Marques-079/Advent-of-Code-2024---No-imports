#Completed 22/04/2025

wire_values = {}
gates = []

with open('day-24/INPUT24.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if ':' in line and '->' not in line:
            wire, value = line.split(':')
            wire_values[wire.strip()] = int(value.strip())

        elif '->' in line:
            parts = line.split()
            if len(parts) == 5:
                in1, op, in2, _, out = parts
            elif len(parts) == 4:  
                op, in1, _, out = parts
                in2 = None
            gates.append((op, in1, in2, out))

#print(gates)
#print(wire_values)#

def XOR(input1, input2):
    if input1 != input2:
        return 1
    return 0

def AND(input1, input2):
    if input1 == 1 and input2 == 1:
        return 1
    return 0

def OR(input1, input2):
    if input1 == 1 or input2 == 1:
        return 1
    return 0

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def solve(gates, wire_values):

    op_map = {
        "XOR": XOR,
        "AND": AND,
        "OR": OR
    }

    pending = gates[:]
    while pending:
        next_pending = []
        for operation, input1, input2, output_name in pending:
            if input1 in wire_values and input2 in wire_values:
                val1 = wire_values[input1]
                val2 = wire_values[input2]
                result = op_map[operation](val1, val2)
                wire_values[output_name] = result
            else:
                next_pending.append((operation, input1, input2, output_name))
        pending = next_pending

    z_wires = sorted([k for k in wire_values if k.startswith('z')])
    binary = ''.join(str(wire_values[z]) for z in reversed(z_wires)) 
    return binary_to_decimal(binary)

dec = solve(gates, wire_values)
print("Decimal result:", dec)







        



