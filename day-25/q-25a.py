#Completed 23/04/2025#

with open("day-25/INPUT25.txt", 'r') as f:
    lines = [line.rstrip() for line in f if line.strip()]

locks = []
keys = []

blocks = [lines[i:i+7] for i in range(0, len(lines), 7)]

for block in blocks:
    if block[0] == "#####":
        locks.append(block)
    elif block[-1] == "#####":
        keys.append(block)

def convert_lock(grid):
    h, w = len(grid), len(grid[0])       
    col_heights = [0] * w
    for col in range(w):                 
        for r in range(1, h - 1):           
            if grid[r][col] == '#':
                col_heights[col] += 1
            else:
                break                       
    return col_heights


def convert_key(grid):
    h, w = len(grid), len(grid[0])
    col_heights = [0] * w
    for col in range(w):
        for r in range(h - 2, 0, -1):      
            if grid[r][col] == '#':
                col_heights[col] += 1
            else:
                break
    return col_heights

def solve(locks, keys):
    total = 0
    locked = [convert_lock(lock) for lock in locks]
    keyed = [convert_key(key) for key in keys]

    for l in locked:
        for k in keyed:
            if all(lh + kh <= 5 for lh, kh in zip(l, k)):
                total += 1
    return total

print(solve(locks,keys))



    


        



