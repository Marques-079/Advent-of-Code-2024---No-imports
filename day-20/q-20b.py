# day20_race.py

# 1) Load the map
with open('day-20/INPUT20.txt') as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
cols = len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

# 2) BFS on track-only (., S, E)
def bfs(start, goal):
    if start == goal:
        return 0
    seen = {start}
    queue = [(start[0], start[1], 0)]
    while queue:
        r, c, d = queue.pop(0)
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                if grid[nr][nc] != '#':    # only walkable
                    if (nr, nc) == goal:
                        return d + 1
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
    return None  # unreachable

# 3) Enumerate cheats that cross exactly one wall
cheats = set()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#':
            continue
        # first move must go into a wall
        for dr1, dc1 in dirs:
            r1, c1 = r + dr1, c + dc1
            if not (0 <= r1 < rows and 0 <= c1 < cols):
                continue
            if grid[r1][c1] != '#':
                continue
            # second move must go back onto track
            for dr2, dc2 in dirs:
                r2, c2 = r1 + dr2, c1 + dc2
                if not (0 <= r2 < rows and 0 <= c2 < cols):
                    continue
                if grid[r2][c2] == '#':
                    continue
                if (r2, c2) == (r, c):
                    continue
                cheats.add(((r, c), (r2, c2)))

# 4) Count how many save ≥100ps (i.e. detour_length - 2 ≥ 100)
count = 0
for (sr, sc), (tr, tc) in cheats:
    detour = bfs((sr, sc), (tr, tc))
    if detour is None:
        continue
    if detour - 2 >= 100:
        count += 1

print("Cheats saving at least 100 ps:", count)
