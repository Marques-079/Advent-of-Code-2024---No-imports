#Completed 09/04/2025

with open('day-12/INPUT12.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

seen = set()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_bounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def dfs(x, y, type):
    seen.add((x, y, type))
    area = 1
    perimeter = 0

    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if not in_bounds(new_x, new_y):
                perimeter += 1
            elif grid[new_x][new_y] !=  type:
                perimeter += 1
            elif (new_x, new_y, type) not in seen:
                seen.add((new_x, new_y, type))
                area += 1 
                queue.append((new_x, new_y))
    return area, perimeter

value = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        type = grid[i][j]
        if (i, j, type) not in seen:
            area, perimeter = dfs(i, j, type)
            value += area * perimeter

print(value)
