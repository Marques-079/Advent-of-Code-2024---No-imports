
with open('day-17/INPUT17.txt', 'r') as f:
    lines = f.read().splitlines()

registers = {}
program = []
output = []

for line in lines:
    if line.startswith("Register A:"):
        registers['A'] = int(line.split(":", 1)[1].strip())
    elif line.startswith("Register B:"):
        registers['B'] = int(line.split(":", 1)[1].strip())
    elif line.startswith("Register C:"):
        registers['C'] = int(line.split(":", 1)[1].strip())
    elif line.startswith("Program:"):
        program = list(map(int, line.split(":", 1)[1].strip().split(",")))

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
    return registers['A'] != 0

def bxc(operand):
    registers['B'] ^= registers['C']

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
        jump = opcode_map[opcode](operand)
        if opcode == 3 and jump:
            ip = operand
        else:
            ip += 2
    else:
        ip += 2

# print(''.join(map(str, output)))      
# print(','.join(map(str, output)))
'''
This one was real tricky so im gonna explain it here so I dont forget how this works if I ever come back to it LOL.
If p < 0 means we have processed our whole list, moving right to left, we feed in len(prgram) -1 so we expect to get p = -1 when A is decoded
'r' is our current A which we are trying to solve (starts at a =0) <<3 converts it into 3bits (8-base) and now we cycle for d in range(8). 

So the reaoson why for d in range(8) is because our A output is 8-based AND if succesful then 'd' is added to our A (although in 8 base it is hard to see)
we check if it is succesful by running the virtual machine - o&7 == o mod(8) - makes our response comparible AKA isolates our change in D to only 
the last digit of the response.

//So all we doing is saying for this guess D once ran thru virtual machine it outputs this guess of A. 
    lets look at last digit of A and check if its a match ALSO to note that we intentionally limit ONE addition 
    to guess A (dictated by guessing D) to ONE value in array programs(g). Ensures we get a match at the end of the day


f the new output of o&7 matches the corresponding program[p] then that addition of D was correct and we call recursively to solve next
recursive call runs on <> olve(p - 1, (r << 3) | d) <> where we shift the p index left and ofc update out 'r' which is now not 0, with the NEW 'd'

'''

g = program

def solve(p, r):
    if p < 0:
        print("Smallest matching value is:", r)
        return True

    for d in range(8):
        a = (r << 3) | d       # build next base‑8 digit
        b = registers['B']     # reset B,C to their initial values
        c = registers['C']
        i = 0

        while i < len(g):
            op = g[i]
            arg = g[i + 1]

            if arg <= 3:
                o = arg
            elif arg == 4:
                o = a
            elif arg == 5:
                o = b
            else: 
                o = c

            if   op == 0:  
                a >>= o
            elif op == 1:  
                b ^= arg
            elif op == 2:  
                b = o & 7
            elif op == 3:  
                if a != 0:
                    i = arg - 2
            elif op == 4:  
                b ^= c
            elif op == 5:  # out → capture and break
                w = o & 7 #Bitwise is same as mod(8) but much faster - constrains w to [0, 7]
                break
            elif op == 6:  
                b = a >> o
            elif op == 7: 
                c = a >> o

            i += 2

        #recurse if matches, thus 'decoding' the next number A must be 
        if w == g[p] and solve(p - 1, (r << 3) | d):
            return True

    return False

solve(len(g) - 1, 0)

print(int("164541160582845", 8))

'''

'''
