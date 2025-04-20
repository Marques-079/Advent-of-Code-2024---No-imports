with open('day-20/INPUT20.txt', 'r') as raw_map:
    grid = [list(line.rstrip('\n')) for line in raw_map if line.strip()]

rows = len(grid)
cols = len(grid[0])
directions = [(-1,0),(1,0),(0,-1),(0,1)]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r,c)
        elif grid[r][c] == 'E':
            end = (r,c)

dist = [[-1]*cols for _ in range(rows)]
sr, sc = start
dist[sr][sc] = 0
q = [(sr, sc)]
while q:
    y, x = q.pop(0)
    for dy, dx in directions:
        ny, nx = y+dy, x+dx
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] != '#' and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

baseline = dist[end[0]][end[1]]
print(f'Baseline is: {baseline}')
cut_off = baseline - 100
print(f'Cut off is: {cut_off}')

save_threshold = 102
count = 0
for y in range(1, rows-1):
    for x in range(1, cols-1):
        if grid[y][x] == '#':
            continue
        d_start = dist[y][x]
        if d_start < 0:
            continue
        for dy, dx in directions:
            wy, wx = y+dy, x+dx
            ty, tx = y+2*dy, x+2*dx
            if 0 <= wy < rows and 0 <= wx < cols and 0 <= ty < rows and 0 <= tx < cols:
                if grid[wy][wx] == '#' and grid[ty][tx] != '#' and dist[ty][tx] >= 0:
                    if dist[ty][tx] - d_start >= save_threshold:
                        count += 1

print(count)
