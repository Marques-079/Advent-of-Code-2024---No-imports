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

def bfs (start_x, start_y, grid):
    queue = [(start_x, start_y)]
    visited = set((start_x, start_y))
    cardinals = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #If you move up then the bracket can face any way.
    #If you move left or right then the bracket must be complementry to the bracket you are calling from

    while queue:
        y, x = queue.pop(0)
        for dy, dx in cardinals:
            ny, nx = y + dy, x + dx #Represent square it wants to move too
            if grid[ny][nx] != '#' and (grid[ny][nx] == '[' or grid[ny][nx] == ']') and not visited:
                if (dy, dx) == (-1, 0) or (dy, dx) == (1, 0): #Vertical movement
                    visited.add((ny, nx))
                    queue.append((ny, nx))
                elif (dy, dx) == (0, -1) or (dy, dx) == (0, 1): #Horinxaontal movement
                    standing_on = grid[y][x]
                    if standing_on == '[' and grid[ny][nx] == ']':
                        visited.add((ny, nx))
                        queue.append((ny, nx))

                    elif standing_on == ']' and grid[ny][nx] == '[':
                        visited.add((ny, nx))
                        queue.append((ny, nx))

            elif grid[ny][nx] == '#' and ((dy, dx) == (-1, 0) or (dy, dx) == (1, 0)) and not visited: #if vertical movement and finds an edge on next
                visited.add(-999, -999) #Stop token to say void action
    return visited

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
