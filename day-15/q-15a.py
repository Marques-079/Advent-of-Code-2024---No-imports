#completed 17/04/2025

with open("day-15/INPUT15.txt") as f:
    lines = f.read().splitlines()

grid_lines = []
directions_line = ""

for line in lines:
    if line.startswith("#") or line.startswith(".") or line.startswith("O") or line.startswith("@"):
        grid_lines.append(line)
    elif set(line).issubset({"^", "v", "<", ">"}):
        directions_line += line

grid = [list(row) for row in grid_lines]
directions = list(directions_line)

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

    if grid[new_x][new_y] == 'O':
        if push_crates(new_x, new_y, move_direction, grid):
            grid[x][y] = '.'
            grid[new_x][new_y] = '@'
            return (new_x, new_y)
        else:
            return robot_pos

    return robot_pos

# Recursively push crates along the given direction.
def push_crates(x, y, direction, grid):
    
    if direction == '^':
        dx, dy = -1, 0
    elif direction == 'v':
        dx, dy = 1, 0
    elif direction == '<':
        dx, dy = 0, -1
    elif direction == '>':
        dx, dy = 0, 1

    next_x, next_y = x + dx, y + dy

    if grid[next_x][next_y] == '#':
        return False

    if grid[next_x][next_y] == '.':
        grid[next_x][next_y] = 'O'
        grid[x][y] = '.'
        return True


    if grid[next_x][next_y] == 'O':
        if push_crates(next_x, next_y, direction, grid):
            grid[next_x][next_y] = 'O'
            grid[x][y] = '.'
            return True
        else:
            return False

    return False

def calculate_gps_sum(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
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
