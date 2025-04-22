#Completed 04/04/2025

with open('day-06/INPUT6.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

n_rows = len(grid)
n_cols = len(grid[0])

cardinal_dict = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

def rotate_right(facing):
    order = ['N', 'E', 'S', 'W']
    idx = order.index(facing)
    return order[(idx + 1) % 4]

def start_pos_and_direction(grid):

    arrow_to_cardinal = {'^': 'N', '>': 'E', 'v': 'S', '<': 'W'}
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] in arrow_to_cardinal:
                initial_dir = arrow_to_cardinal[grid[i][j]]
                grid[i][j] = '.'  
                return (i, j), initial_dir
    return None, None

def in_bounds(node):
    x, y = node
    return 0 <= x < n_rows and 0 <= y < n_cols

position, cardinal = start_pos_and_direction(grid)
if position is None:
    print("No starting position found.")
    exit()

visited = set()
visited.add(position)
steps = 1  

while True:

    dx, dy = cardinal_dict[cardinal]
    next_pos = (position[0] + dx, position[1] + dy)
    
    if not in_bounds(next_pos):
        break
    
    if grid[next_pos[0]][next_pos[1]] == '#':
        cardinal = rotate_right(cardinal)
        continue
    else:
      
        position = next_pos
        visited.add(position)
        steps += 1

print(len(visited))


