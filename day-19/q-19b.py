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
    
    if design == '':
        return 1
    
    total = 0
    if design[0] in combos: 
        for piece in combos[design[0]]: #iterator
            if design.startswith(piece):
                cut = len(piece)
                total += piece_up(design[cut:], memo)

    '''
    The logic here uses memo as a HUGE time save whats happening is:
    When it reaches the end of a string solve (alternatively 0 if unsolvable) a number 1 is returned indicating 1 way of solving the design
    After bubbling up one function this (1) is added to the total and then for this given snapshot of design a 1 is assigned in the memo dict
    Notice how the only exit from the function is <> return total <> meaning the totals/combos are cumulative (as they should be)
    Thus at a later date if we have already done the work we can skip the calculations because we already know the combos needed in memo[design]
    '''
    memo[design] = total 
    return total
                    
count = 0
for d in designs:
    count+= piece_up(d, {})

print(count) 
