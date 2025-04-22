
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
            else:
                op, in1, _, out = parts
                in2 = None
            gates.append((op, in1, in2, out))

def make_wire(char, i):
    return f'{char}{i:02d}'
def make_x(i): 
    return make_wire('x', i)
def make_y(i): 
    return make_wire('y', i)
def make_z(i): 
    return make_wire('z', i)

null_values = {}
for i in range(45):
    null_values[make_x(i)] = 0
    null_values[make_y(i)] = 0

'''
So we expcect for all 9 combos it should have the same output which is the target outpujt.
 Also because we arent dealing with one node do we set all other bits in the X and Y input to 0
 Except the one we are using and then bubble that up to see if our output matches
'''

def init_values(bit, x, y, carry): #Sets up one test bit as 1 and rest 0
    vals = null_values.copy()
    vals[make_x(bit)]   = x
    vals[make_x(bit-1)] = carry
    vals[make_y(bit)]   = y
    vals[make_y(bit-1)] = carry
    return vals

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

operators = {'AND': AND, 'XOR': XOR, 'OR': OR}

# Evaluate any wire recursively
def get_value(wire, values, wire_map):
    if wire in values: #if hits a bottom node in values then return value
        return values[wire]
    op, i1, i2 = wire_map[wire]
    v1 = get_value(i1, values, wire_map)
    v2 = get_value(i2, values, wire_map)
    res = operators[op](v1, v2)
    values[wire] = res #if values are returned from bits then calculate required operation
    return res

# Find the gate that does target_op on at least those inputs
def find_wire(target_op, ins_set, wire_map):
    for out, (op, i1, i2) in wire_map.items():
        if op == target_op and ins_set.issubset({i1, i2}):
            return out
    return None

def solve_part2(gates, wire_values):

    wire_map = {out:(op,i1,i2) for (op,i1,i2,out) in gates}
    swapped = set()

    '''
    okay so essentially we divide the bits into single bits and we know each one must work for all 8 combos and run consistenyly. 
    If error there must be something wrong with out ciricut. the method to ad bits is a 1 bit fuller adder and 
    Thus there must be a connection wrong in the full adder.
    So we look at standard full adder architecure and compare it to our current broken circut and 
    the mismatch we identify is the faulty wire
    '''

    def fix_bit(bit):
        cx, cy = make_x(bit), make_y(bit)
        px, py = make_x(bit-1), make_y(bit-1)

        cxor   = find_wire('XOR', {cx, cy}, wire_map)
        pxor   = find_wire('XOR', {px, py}, wire_map)
        dcarry = find_wire('AND', {px, py}, wire_map)
        rcarry = find_wire('AND', {pxor},     wire_map)
        carry  = find_wire('OR',  {dcarry, rcarry}, wire_map)
        zsum   = find_wire('XOR', {cxor, carry},   wire_map)

        if zsum is None:
            _, z1, z2 = wire_map[make_z(bit)]
            ins = {z1, z2}
            w1, w2 = ins ^ {cxor, carry}
        else:
            w1, w2 = zsum, make_z(bit)

        # perform the swap in the map
        wire_map[w1], wire_map[w2] = wire_map[w2], wire_map[w1]
        return {w1, w2}
    '''
    So essentially our whole cicut is a bunch of 1 bit adders?
    Furhtermore we can identify a wrong wire exactly by applying the standard 1 bit adder formula and build up from base bits X,Y
    In the question it means the faulty wire swap can be within the same 1bit adder or a potentially different adder
    We can only confidently swap wires as we work because we know pairs have been swapped only 
    And thus we do not have to worry about a full random scramble 
    '''
    for bit in range(1, 45):
        #test all 8 cases; if any fails, we must fix that bit
        bad = False
        for x in (0,1):
            for y in (0,1):
                for c in (0,1):
                    vals = init_values(bit, x, y, c)
                    got = get_value(make_z(bit), vals, wire_map) 
                    if got != (x ^ y ^ c): #“Does the output the circuit gave me (got) match what a correct adder should have produced for these inputs?”
                        bad = True
                        break
                if bad: 
                    break
            if bad: 
                break
        if bad:
            swapped |= fix_bit(bit)

    return ','.join(sorted(swapped))

answer2 = solve_part2(gates, wire_values)
print("Part 2: Swapped wires:", answer2)
