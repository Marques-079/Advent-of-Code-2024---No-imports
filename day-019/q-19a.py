#Completed 20/04/2025

with open('day-19/input19.txt') as f:
    lines = [line.strip() for line in f]

split_index = lines.index("") 
towel_patterns = lines[0].replace(" ", "").split(",")
designs = lines[split_index + 1:] 

combos = {}
for pattern in towel_patterns:
    first = pattern[0]
    if first not in combos:
        combos[first] = []
    combos[first].append(pattern)


def piece_up(design, memo):
    if design in memo:
        return memo[design]

    if design == memo:
        return True
    if design == '':
        return True
    
    if design[0] not in combos:
        memo[design] = False
        return False
    
    for piece in combos[design[0]]:
        if design.startswith(piece):
            cut = len(piece)
            if piece_up(design[cut:], memo):
                memo[design] = True #Cut of design in this moment is solvable // design is slowly sliced as we try combos
                return True
    memo[design] = False
    return False

count = 0
for d in designs:
    if piece_up(d, {}):
        count += 1

print(count) 
