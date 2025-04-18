with open('day-17/INPUT17.txt', 'r') as f:
    lines = f.read().splitlines()

registers = {}
program = []
output=  []

for line in lines:
    if line.startswith("Register A:"):
        registers['A'] = int(line.split(":")[1].strip())
    elif line.startswith("Register B:"):
        registers['B'] = int(line.split(":")[1].strip())
    elif line.startswith("Register C:"):
        registers['C'] = int(line.split(":")[1].strip())
    elif line.startswith("Program:"):
        program = list(map(int, line.split(":")[1].strip().split(",")))
        
print(program)
print(registers)

def resolve_combo_operand(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']

def adv(operand):
    denom = resolve_combo_operand(operand)
    registers['A'] //= (2 ** denom)

def bxl(operand):
    registers['B'] ^= operand

def bst(operand):
    value = resolve_combo_operand(operand)
    registers['B'] = value % 8

def jnz(operand):
    operand = operand
    return registers['A'] != 0  # Return True if we should jump

def bxc(operand):
    operand = operand
    registers['B'] ^= registers['C']  # Operand is ignored

def out(operand):
    value = resolve_combo_operand(operand) % 8
    output.append(value)

def bdv(operand):
    denom = resolve_combo_operand(operand)
    registers['B'] = registers['A'] // (2 ** denom)

def cdv(operand):
    denom = resolve_combo_operand(operand)
    registers['C'] = registers['A'] // (2 ** denom)


opcode_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

ip = 0
while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]

    if opcode in opcode_map:
        should_jump = opcode_map[opcode](operand)
        if opcode == 3 and should_jump:  #Special case if it calls JNZ
            ip = operand
        else:
            ip += 2

print(''.join(map(str, output)))
#print(','.join(map(str, output)))






