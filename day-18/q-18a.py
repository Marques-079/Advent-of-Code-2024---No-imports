#Completed 20/04/2025#

coordinates = []
with open('day-18/INPUT18.txt', 'r') as f:
    for line in f:
        x, y = map(int, line.strip().split(','))
        coordinates.append((x, y))

grid = []
for row_index in range(71):
    row = []
    for col_index in range(71):
        row.append('.')
    grid.append(row)

for x, y in coordinates[:1025]:
    grid[y][x] = '#'

def heuristic(r, c, goal_r, goal_c):
    return abs(r - goal_r) + abs(c - goal_c)

def a_star(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    start = (0, 0)
    end = (70, 70)

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

print(a_star(grid))
