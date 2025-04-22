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

total_score = 0
for start_row, start_col in trailheads:
    visited = set()
    queue = [(start_row, start_col)]
    visited.add((start_row, start_col))
    found_nines = set()
    
    while queue:
        r, c = queue.pop(0)

        if grid[r][c] == 9:
            found_nines.add((r,c))

        for nr, nc in neighbors(r, c, len(grid), len(grid[0])):
            if (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1 and bounds_check(nr, nc, len(grid), len(grid[0])):   
                visited.add((nr, nc))
                queue.append((nr, nc))

    total_score += len(found_nines)
print(total_score)





    
