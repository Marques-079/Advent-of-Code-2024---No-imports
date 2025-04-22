#Completed 22/04/2025

code_list = open("day-21/INPUT21.txt").read().splitlines()

def pairwise(iterable): #Maps out start -> end coords from the code
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return
    for second in it:
        yield first, second
        first = second


def permutations(seq): #Once a move order is found there may be other combos of the moves which achieve higher efficiency
    if len(seq) <= 1:
        yield tuple(seq)
    else:
        for i in range(len(seq)):
            for p in permutations(seq[:i] + seq[i + 1 :]):
                yield (seq[i],) + p


INF = float("inf") #Baseline

dir_lookup = { #Faster lookups for interactions within directions key pads
    ("A", "A"): "A", ("^", "^"): "A", (">", ">"): "A",
    ("v", "v"): "A", ("<", "<"): "A", ("A", "^"): "<A",
    ("^", "A"): ">A", ("A", ">"): "vA", (">", "A"): "^A",
    ("v", "^"): "^A", ("^", "v"): "vA", ("v", "<"): "<A", 
    ("<", "v"): ">A", ("v", ">"): ">A", (">", "v"): "<A", 
    ("A", "v"): "v<A", ("v", "A"): ">^A", ("A", "<"): "v<<A",
    ("<", "A"): ">>^A", (">", "<"): "<<A", ("<", ">"): ">>A",
    ("<", "^"): ">^A", ("^", "<"): "v<A", (">", "^"): "<^A",
    ("^", ">"): "v>A",
}

dir_axes = [
    [("^", -1), ("v", 1)],  # vertical moves (index 0)
    [("<", -1), (">", 1)],  # horizontal moves (index 1)
]

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [" ", "0", "A"],
]

numpad_pos = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    " ": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}

dirpad = [
    [" ", "^", "A"],
    ["<", "v", ">"],
]

dirpad_pos = {
    " ": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def dir_dfs(key_start, key_end, depth=0):
    '''
     DFS for a lineup of keypads, if depth (1 keypad) == 0 then we are at base layer and can return normal arm movements
     if not then we must recurse down by starting at A and (ending at A) then moving the required arm positions.
     This is because for each robot we have to end at 'A' aka press the button to pass our movement foward and this next move starts at A
     Next we need to seperate the string into sets of (start, end) which we then call dir_difs on again -> concatenate the output
    '''
    if depth == 0:
        return dir_lookup[key_start, key_end]

    inner = dir_dfs(key_start, key_end, depth - 1)
    result = ""
    for k0, k1 in pairwise("A" + inner):
        result += dir_lookup[k0, k1]
    return result


def num_solve(key_start, key_end):
    '''
    This code looks at start and end key on numeric pad and finds A method of moving from start to finish
    Then runs perms to find all possible combos (simular to what BFS would do) much more efficient
    '''
    r0, c0 = numpad_pos[key_start]
    r1, c1 = numpad_pos[key_end]
    dr, dc = r1 - r0, c1 - c0
    vert_key, _ = dir_axes[0][dr > 0]
    horiz_key, _ = dir_axes[1][dc > 0]

    '''
    Corner avoidance logic
    Essentially if in danger zones so bottom row or leftmost column is in start or finish coords then force move right/up
    then uodate start coords and run basic mapping normally BUT we have to add the start_move to the front of queue after A (where we start)
    '''
    initial_move = ""
    move_seq = ""
    if (r0 == 3 or r1 == 3) and (c0 == 0 or c1 == 0): #Starting or ending on the bottom row
        if c0 == 0: #starting left most column
            initial_move = ">"
            move_seq = vert_key * abs(dr) + horiz_key * (abs(dc) - 1)
        else:
            initial_move = "^"
            move_seq = vert_key * (abs(dr) - 1) + horiz_key * abs(dc)
    else:
        move_seq = vert_key * abs(dr) + horiz_key * abs(dc) #normal movements

    candidates = [
        "A" + initial_move + "".join(p) + "A" for p in set(permutations(move_seq))
    ]

    '''
    From the base commands from numeric keypad we pass on to dirs, for the possible perms of paths between the concatenated 
    pairwise codes, and we return the lowest lengthed sequence out of those possible perms on the base numeric keypad
    '''
    best_len = INF
    best_sequence = ""
    for cand in candidates:
        sequence = "".join(
            dir_dfs(k0, k1, depth=1) for k0, k1 in pairwise(cand)
        )
        if len(sequence) < best_len:
            best_len = len(sequence)
            best_sequence = sequence

    return best_sequence


overall_score = 0
for code in code_list:
    repeat = int(code[:-1])
    seq = "".join(num_solve(a, b) for a, b in pairwise("A" + code))
    overall_score += len(seq) * repeat
    print(f"Start Code {code} | Lowest lenght found: {len(seq)} | Complexity: {len(seq)*repeat}")

print("Total score", overall_score)
