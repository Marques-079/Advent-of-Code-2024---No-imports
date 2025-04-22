#Completed 16/04/2025

def read_input(filename):
    p_v = []
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            p_str = parts[0].split('=')[1]
            v_str = parts[1].split('=')[1]
            px, py = map(int, p_str.split(','))
            vx, vy = map(int, v_str.split(','))
            positions = (px, py)
            velocities = (vx, vy)
            p_v.append([positions, velocities])
    return p_v

def move(curr_position, velocity):
    x, y = curr_position
    vx, vy = velocity
    dx, dy = x + vx, y + vy
    if 0 <= dx <= 100 and 0 <= dy <= 102:
        return dx, dy
    else:
        new_x = (x + vx) % 101
        new_y = (y + vy) % 103
        return new_x, new_y
    
def largest_connected_area(positions):
    grid = [['.' for _ in range(101)] for _ in range(103)]
    for x, y in positions:
        grid[y][x] = '#'

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def bfs(start_y, start_x):
        queue = [(start_y, start_x)]
        visited[start_y][start_x] = True
        area = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            y, x = queue.pop(0)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols:
                    if not visited[ny][nx] and grid[ny][nx] == '#':
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        area += 1
        return area

    max_area = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '#' and not visited[y][x]:
                max_area = max(max_area, bfs(y, x))

    return max_area


def print_grid(positions, sec):
    area = largest_connected_area(positions)
    if area > 100:
        grid = [['.' for _ in range(101)] for _ in range(103)]
        for x, y in positions:
            grid[y][x] = '#'

        print(f"Second: {sec}")
        for row in grid:
            print(''.join(row))
        print("\n")
    else:
        None

def simulate_and_print(p_v):
    for sec in range(1, 10000):
        for i in range(len(p_v)):
            curr_pos = p_v[i][0]
            velocity = p_v[i][1]
            new_pos = move(curr_pos, velocity)
            p_v[i][0] = new_pos
        positions = [pv[0] for pv in p_v]

        print_grid(positions, sec)
    


input_file = "day-14/INPUT14.txt"
p_v = read_input(input_file)
simulate_and_print(p_v)

