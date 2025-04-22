#Completed 07/04/2025

grid = []
with open("day-10/INPUT10.txt", 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            row = [int(ch) for ch in line]
            grid.append(row)

def neighbors(r, c, rows, cols):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def bounds_check(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

trailheads = [(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]

cols = len(grid[0])
rows = len(grid)
dp = [[-1]*cols for _ in range(rows)]

def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    if grid[r][c] ==9:
        return 1    
    
    current_elevation = grid[r][c]
    total = 0
    for nr, nc in neighbors(r, c, rows, cols):
        if bounds_check(nr, nc, rows, cols) and (grid[nr][nc] - current_elevation == 1):
            total += dfs(nr, nc)

    dp[r][c] = total
    return total

sum = 0
for r, c in trailheads:
    sum += dfs(r, c)

print(sum)





    
