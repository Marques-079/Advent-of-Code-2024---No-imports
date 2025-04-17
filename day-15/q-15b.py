#completed 17/04/2025

with open("day-15/INPUT15.txt") as f:
    lines = f.read().splitlines()

grid_lines = []
expanded_grid = []
directions_line = ""

for line in lines:
    if line.startswith("#") or line.startswith(".") or line.startswith("O") or line.startswith("@"):
        grid_lines.append(line)
    elif set(line).issubset({"^", "v", "<", ">"}):
        directions_line += line

grid = [list(row) for row in grid_lines]
directions = list(directions_line)
cardinals = [(-1, 0), (1, 0), (0, -1), (0, 1)] #NSWE

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            grid[i][j] = "@,."
        elif grid[i][j] == "O":
            grid[i][j] = "[,]"
        elif grid[i][j] == "#":
            grid[i][j] = "#,#"
        elif grid[i][j] == ".":
            grid[i][j] = ".,."
        else:
            print("Error: Unknown character in grid")

for row in grid:
    new_row = []
    for cell in row:
        left, right = cell.split(",")
        new_row.append(left)
        new_row.append(right)
    expanded_grid.append(new_row)

grid = expanded_grid
directions = list(directions_line)
cardinals = [(-1, 0), (1, 0), (0, -1), (0, 1)] #NSWE

def bfs(start_x, start_y, grid, direction):

    push_dx, push_dy = (-1, 0) if direction == '^' else (1, 0)

    visited = [(start_x, start_y)]
    queue   = [(start_x, start_y)]
    seen    = {(start_x, start_y)}

    while queue:
        x, y = queue.pop(0)

        nx, ny = x + push_dx, y + push_dy
        if grid[nx][ny] == '#':
            return False

        #if it's another crate half, follow it
        if grid[nx][ny] in ('[', ']') and (nx, ny) not in seen:
            seen.add((nx, ny))
            queue.append((nx, ny))
            visited.append((nx, ny))

        if grid[x][y] in ('[', ']'):
            if grid[x][y] == '[':
                px, py = x, y + 1
                want = ']'
            else:
                px, py = x, y - 1
                want = '['

            if grid[px][py] == want and (px, py) not in seen:
                seen.add((px, py))
                queue.append((px, py))
                visited.append((px, py))

    push_crates(visited, direction, grid)
    return True

def push_crates(visited, direction, grid):

    #sort so that we move the furthest‐away crates first
    if direction == 'v':
        visited_sorted = sorted(visited, key=lambda c: c[0], reverse=True)
        dx, dy = 1, 0
    else:
        visited_sorted = sorted(visited, key=lambda c: c[0])
        dx, dy = -1, 0

    for x, y in visited_sorted:
        nx, ny = x + dx, y + dy
        grid[nx][ny] = grid[x][y]
        grid[x][y] = '.'


def push_crates_horizontal(visited, direction, grid):

    if direction == '>':
        #push right: start from largest column index
        visited_sorted = sorted(visited, key=lambda c: c[1], reverse=True)
        dx, dy = 0, 1
    else:
        #push left: start from smallest column index
        visited_sorted = sorted(visited, key=lambda c: c[1])
        dx, dy = 0, -1

    for x, y in visited_sorted:
        nx, ny = x + dx, y + dy
        grid[nx][ny] = grid[x][y]
        grid[x][y] = '.'


def bfs2(start_x, start_y, direction, grid):

    dx, dy = (0, -1) if direction == '<' else (0, 1)
    visited = []
    x, y = start_x, start_y

    #move forward until we hit floor or a wall
    while True:
        if grid[x][y] == '#':
            return False
        if grid[x][y] not in ('[', ']'):
            break

        #collect this half
        if (x, y) not in visited:
            visited.append((x, y))

        #collect its partner half
        if grid[x][y] == '[':
            px, py = x, y + 1
        else:
            px, py = x, y - 1

        if grid[px][py] in ('[', ']') and (px, py) not in visited:
            visited.append((px, py))

        #step forward
        x, y = x + dx, y + dy

    # all clear then perform the push
    push_crates_horizontal(visited, direction, grid)
    return True

        
#Moving logic
def move_robot(robot_pos, move_direction, grid):
    x, y = robot_pos
    if move_direction == '^':
        dx, dy = -1, 0
    elif move_direction == 'v':
        dx, dy = 1, 0
    elif move_direction == '<':
        dx, dy = 0, -1
    elif move_direction == '>':
        dx, dy = 0, 1
    else:
        return robot_pos  

    new_x, new_y = x + dx, y + dy

    if grid[new_x][new_y] == '#':
        return robot_pos

    if grid[new_x][new_y] == '.':
        grid[x][y] = '.'
        grid[new_x][new_y] = '@'
        return (new_x, new_y)
    
    #If robot is moving horinzontal and crate
    if (grid[new_x][new_y] == '[' or grid[new_x][new_y] == ']') and move_direction in ['<', '>']:
        if bfs2(new_x, new_y, move_direction, grid):
            grid[x][y] = '.'
            grid[new_x][new_y] = '@'
            return (new_x, new_y)
        else:
            return robot_pos

    #If robot is moving vertical and crate
    if (grid[new_x][new_y] == '[' or grid[new_x][new_y] == ']') and move_direction in ['^', 'v']:
        if bfs(new_x, new_y, grid, move_direction):
            grid[x][y] = '.'
            grid[new_x][new_y] = '@'
            return (new_x, new_y)
        else:
            return robot_pos  
    return robot_pos


def calculate_gps_sum(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '[':
                total += 100 * row + col  
    return total

def simulate(grid, directions):
    robot_pos = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                robot_pos = (i, j)
                break
        if robot_pos is not None:
            break

    if robot_pos is None:
        print("Robot not found.")
        return

    for move_direction in directions:
        robot_pos = move_robot(robot_pos, move_direction, grid)
    return grid

simulate(grid, directions)
#print(grid)
result = calculate_gps_sum(grid)
print("Sum of all boxes GPS coords", result)
