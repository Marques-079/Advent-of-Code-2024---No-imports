#Completed 18/04/2025

with open("day-16/input16.txt") as f:
    grid = [list(line.strip()) for line in f]

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "E":
            end = (r, c)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW


def heuristic(r, c, goal_r, goal_c):
    return abs(r - goal_r) + abs(c - goal_c)

def a_star(grid):
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)

    start_state = (start[0], start[1], 1)  #    start facing East
    g_cost = {start_state: 0}
    priorityq = [(heuristic(start[0], start[1], end[0], end[1]), 0, start[0], start[1], 1)]
    visited = set()

    while priorityq:
        priorityq.sort(reverse=True)
        f, cost, r, c, dir = priorityq.pop()

        if (r, c, dir) in visited:
            continue
        visited.add((r, c, dir))

        if (r, c) == end:
            return cost, g_cost

        # Move forward
        dr, dc = directions[dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            new_state = (nr, nc, dir)
            new_g = cost + 1
            if new_state not in g_cost or new_g < g_cost[new_state]: #Either the state is band new or the cost is less than the previous
                g_cost[new_state] = new_g                            #cost recorded in g_cost for the given (coords, directions)
                h = heuristic(nr, nc, end[0], end[1])
                priorityq.append((new_g + h, new_g, nr, nc, dir))

        # Turn left
        nd_left = (dir - 1) % 4
        new_state = (r, c, nd_left)
        new_g = cost + 1000
        if new_state not in g_cost or new_g < g_cost[new_state]:
            g_cost[new_state] = new_g
            h = heuristic(r, c, end[0], end[1])
            priorityq.append((new_g + h, new_g, r, c, nd_left))

        # Turn right
        nd_right = (dir + 1) % 4
        new_state = (r, c, nd_right)
        new_g = cost + 1000
        if new_state not in g_cost or new_g < g_cost[new_state]:
            g_cost[new_state] = new_g
            h = heuristic(r, c, end[0], end[1])
            priorityq.append((new_g + h, new_g, r, c, nd_right))

    return -1, g_cost

def trace_all_shortest_paths(g_cost, end, min_cost, directions):
    queue = []
    path_tiles = set()

    for dir in range(4):
        state = (end[0], end[1], dir)
        if g_cost.get(state) == min_cost:
            queue.append(state)

    while queue:
        r, c, dir = queue.pop(0)
        path_tiles.add((r, c))

        current_cost = g_cost[(r, c, dir)]

        dr, dc = directions[dir]
        prev_r = r - dr
        prev_c = c - dc
        prev_state = (prev_r, prev_c, dir)

        if prev_state in g_cost and g_cost[prev_state] + 1 == current_cost:
            queue.append(prev_state)

        for turn in [-1, 1]:
            from_dir = (dir + turn) % 4
            turn_state = (r, c, from_dir)
            if turn_state in g_cost and g_cost[turn_state] + 1000 == current_cost:
                queue.append(turn_state)

    return path_tiles


min_cost, g_costs = a_star(grid)
valid_coords = trace_all_shortest_paths(g_costs ,end, min_cost, directions)
print(len(valid_coords))

