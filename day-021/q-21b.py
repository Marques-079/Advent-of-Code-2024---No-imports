#Completed 22/04/2025

code_list = open("day-21/INPUT21.txt").read().splitlines()
INF = float("inf") #Baseline

def pairwise(iterable):                      
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return
    for item in it:
        yield prev, item
        prev = item


def permutations(seq):                    
    if len(seq) <= 1:
        yield (seq[0],) if seq else ()
        return
    for i in range(len(seq)):
        for p in permutations(seq[:i] + seq[i + 1 :]):
            yield (seq[i],) + p

dir_lookup = {
    ('A', 'A'): 'A',  ('^', '^'): 'A', ('>', '>'): 'A', ('v', 'v'): 'A',
    ('<', '<'): 'A',  ('A', '^'): '<A', ('^', 'A'): '>A', ('A', '>'): 'vA',
    ('>', 'A'): '^A', ('v', '^'): '^A', ('^', 'v'): 'vA', ('v', '<'): '<A',
    ('<', 'v'): '>A', ('v', '>'): '>A', ('>', 'v'): '<A',

    ('A', 'v'): '<vA', ('v', 'A'): '^>A', ('A', '<'): 'v<<A', ('<', 'A'): '>>^A',
    ('>', '<'): '<<A', ('<', '>'): '>>A', ('<', '^'): '>^A', ('^', '<'): 'v<A',
    ('>', '^'): '<^A', ('^', '>'): 'v>A',
}

dir_axes = [
    [("^", -1), ("v",  1)],   # vertical moves
    [("<", -1), (">",  1)],   # horizontal moves
]

numpad_pos = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    " ": (3, 0), "0": (3, 1), "A": (3, 2),
}


memo_dir = {}                      
def dir_len(s, depth= 25):
    """
    Main difference here is in the dir function here. 
    Instead of passing around the actuals strings it passes around integer values. 
    Because we know the best methods to naviagate the directional keypad its very fast 0(1) lookup.
    After receving a string of dirs and then splitting it pairwise we apply the pass down expansions 
    """
    if depth == 0:
        return len(s) #KEYSTEP WE PASS UP INTEGERS INSTEAD OF STRINGS
    cached = memo_dir.get((s, depth)) #memory here
    if cached is not None:
        return cached

    total = 0
    for a, b in pairwise("A" + s):      # every hop starts at 'A' ->>> For loop is crucial for memorisation as we move down branch we remeber all calcs
        ''' <- Applying expansions here '''
        total += dir_len(dir_lookup[a, b], depth - 1)
        '''
        Expands the pairwise into the standard AxxxA format which doesnt explode string. Calls recursively on this and splits again.
        Difference between A and B code is building these strings be realtively small.
        Its the concatenation which takes the most time?
        '''
    memo_dir[s, depth] = total #S = string and depth = depth
    return total


def num_solve(k0, k1):

    r0, c0 = numpad_pos[k0]
    r1, c1 = numpad_pos[k1]
    dr, dc = r1 - r0, c1 - c0
    vert_key = dir_axes[0][dr > 0][0]
    horiz_key = dir_axes[1][dc > 0][0]

    # Corner avoidance hack for the blank in bottom‑left
    initial_move = ""
    if (r0 == 3 or r1 == 3) and (c0 == 0 or c1 == 0):
        if c0 == 0:                     # starting in left column
            initial_move = ">"
            move_seq = vert_key * abs(dr) + horiz_key * (abs(dc) - 1)
        else:                           # starting in bottom row
            initial_move = "^"
            move_seq = vert_key * (abs(dr) - 1) + horiz_key * abs(dc)
    else:
        move_seq = vert_key * abs(dr) + horiz_key * abs(dc)

    candidates = (
        f"{initial_move}{''.join(p)}A" for p in set(permutations(move_seq))
    )

    best_string, best_len = "", INF
    for cand in candidates:
        score = dir_len(cand)
        if score < best_len:
            best_string, best_len = cand, score
    return best_string


def solve(code):

    augmented = "A" + code

    total_length = 0
    for current_key, next_key in pairwise(augmented):
        best_move = num_solve(current_key, next_key)
        hop_cost = dir_len(best_move)

        total_length += hop_cost

    return total_length


overall_score = 0

for code in code_list:
    repeat = int(code[:-1])            
    length = solve(code)
    overall_score += length * repeat
    print(f"Start Code {code} | Best length: {length} | Complexity: {length * repeat}")

print("Total score", overall_score)
