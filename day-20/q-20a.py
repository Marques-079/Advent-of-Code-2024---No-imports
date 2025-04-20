with open('day-20/INPUT20.txt', 'r') as raw_map:
    grid = [list(line) for line in raw_map.read().strip().splitlines()]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "E":
            end = (r, c)
#print(start)
#print(end)

#Find the baseline fastest without cheating
def heuristic(r, c, goal_r, goal_c):
    return abs(r - goal_r) + abs(c - goal_c)

def a_star(grid, rows, cols):
    
    g_cost = {start: 0}
    priorityq = [(heuristic(*start, *end), 0, start[0], start[1])]  
    visited = set()

    while priorityq:
        
        priorityq.sort(reverse=True)
        f, g, r, c = priorityq.pop()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == end:
            return g 

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                neighbor = (nr, nc)
                new_g = g + 1
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    h = heuristic(nr, nc, *end)
                    f_score = new_g + h
                    priorityq.append((f_score, new_g, nr, nc))

    return -1 

def can_cheat(x, y, dir): #From a tile given direction can it jump

    dx, dy = directions[dir]
    new_x, new_y = x + dx, y + dy
    jump_x, jump_y = x + dx + dx, y + dy + dy

    if 0 <= jump_x < rows and 0 <= jump_y < cols: #Jump after the wall is a valid location
        if grid[new_x][new_y] == '#' and grid[jump_x][jump_y] == '.':
            return True, (jump_x, jump_y)
    return False, (x, y) #Returns either True and the new jumped coords or false and same 'staring' coords.

def scan(grid, start, end, cut_off):
    seen = set()
    queue = []
    queue.append((*start, False, 0 )) #coords, cheated, cost
    total = 0
    checker = 1
    prune_count = 1


    while queue:
        print(checker)
        checker += 1
        x, y, cheated, time = queue.pop(0)

        if (x,y) == end and cheated == True:
            total += 1
            continue
        elif (x,y) == end and cheated == False:
            total += 0
            continue
        
        if (x, y, cheated) in seen:
            continue

        if time > cut_off:
            print(f' Prune count is {prune_count}')
            prune_count +=1
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == '.':
                seen.add((x, y, cheated))
                queue.append((nx, ny, cheated, time + 1))
        
        if not cheated:
            for cardinals in range(4):
                success, (jx, jy) = can_cheat(x, y, cardinals)
                if success:
                    seen.add((x, y, cheated))
                    queue.append((jx, jy, True, time + 2)) 

    return total

baseline = a_star(grid, rows, cols)
print(f'Baseeline is: {baseline}')
cut_off = baseline - 100
print(f'Cut off is {cut_off}')

count = scan(grid, start, end, cut_off)
print(count)



