#Completed 21/04/2025

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


def mini_bfs(sy, sx, d0):

    '''
    Runs a 20 tile radius BFS around the starting point regardless of walls or tiles. Think of it as becoming a ghost for 19 tiles.
    Thus any tile it reaches at the end or within its 19 tile ghost mode should be marked as a possible stop tile - all 19 phases 
    do not have to be used and can be used intermitenly. 

    These possible coordinates are recorded into seen dictionary with the value of distance 
    '''
    seen = {(sy,sx): 0}
    q    = [(sy,sx,0)]
    endpoints = {}
    while q:
        r, c, d = q.pop(0)
        if d == 20: 
            continue
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < rows and 0 <= nc < cols): 
                continue
            nd = d+1
            if ((nr,nc) not in seen) or nd < seen[(nr,nc)]:
                seen[(nr,nc)] = nd
                q.append((nr,nc,nd)) 

    '''
    With distance and the ending coordinates we can find if the jump was useful. Must pass the following checks tho
    Cannot be the starting square (that is marked in seen), Cannot be ending on a wall, distance cannot be traversing away 
    from the goal. Jump spot cant land on a unexplored region market '-1' and cant traversal away from goal d2 <- d0

    Thus an endpoint is valid if the without_cheats is normal_dist - cheat dist = distance_saved, if above/equal threshold
    then its safe to total that jump
    '''

    for (r2,c2), L in seen.items():
        if L == 0 or grid[r2][c2]== '#': 
            continue
        d2 = dist[r2][c2]
        if d2 < 0 or d2 <= d0: 
            continue
        if (d2 - d0) - L >= 100:
            endpoints[(r2,c2)] = True
    return len(endpoints)

count = 0
for y in range(1, rows-1):
  for x in range(1, cols-1):
    d0 = dist[y][x]
    if d0 < 0: 
        continue
    if any(grid[y+dy][x+dx]=='#' for dy,dx in directions):
      count += mini_bfs(y, x, d0)

print(count)

        


