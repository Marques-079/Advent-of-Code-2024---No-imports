#Completed 18/04/2025

with open("day-16/input16.txt") as f:
    grid = [list(line.strip()) for line in f]

def dijkstras(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  #NESW

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)
    priorityq = [(0, start[0], start[1], 1)] #(current cost, start X coord, start Y coord, direction corresponding to directions)
    visited = set()

    while priorityq:
        priorityq.sort(reverse =True) 
        cost, r, c, dir = priorityq.pop()

        if (r, c, dir) in visited: #if same state has been found then skip because this is an infinite loop
            continue
        visited.add((r, c, dir)) #if unseenn state then add to visited for later use

        if (r, c) == end:
            return cost
        
        #Move straight
        dr, dc = directions[dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            priorityq.append((cost + 1, nr, nc, dir))

        #Try turning left
        nd_left = (dir - 1) % 4
        if (r, c, nd_left) not in visited:
            priorityq.append((cost + 1000, r, c, nd_left))

        #Try turning right
        nd_right = (dir + 1) % 4
        if (r, c, nd_right) not in visited:
            priorityq.append((cost + 1000, r, c, nd_right))

    return -1

print(dijkstras(grid))








