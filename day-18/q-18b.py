#Completed 20/04/2025

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

#Real code below

#Binary search optimiser
def is_blocked(k, coordinates):
    grid = [['.' for _ in range(71)] for _ in range(71)]
    
    for i in range(k):
        x, y = coordinates[i]
        grid[y][x] = '#'
    
    return a_star(grid) == -1  

def add_byte(count, grid):
    x, y =coordinates[count]
    grid[y][x] = '#'
    return x, y

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

def simulate(grid, coordinates):
    left = 0 
    right = len(coordinates)

    while left < right:
        mid = (left + right) // 2
        if is_blocked(mid, coordinates):
            right = mid
        else:
            left = mid + 1

    x, y = coordinates[left - 1]
    print(f"{x},{y}")

simulate(grid, coordinates)

