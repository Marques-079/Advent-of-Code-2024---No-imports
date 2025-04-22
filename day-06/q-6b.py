#Completed 04/04/2025

with open('day-6/INPUT6.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

n_rows = len(grid)
n_cols = len(grid[0])

cardinal_dict = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

def rotate_right(facing):
    order = ['N', 'E', 'S', 'W']
    idx = order.index(facing)
    return order[(idx + 1) % 4]

def find_start(grid):
    arrow_to_cardinal = {'^': 'N', '>': 'E', 'v': 'S', '<': 'W'}
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] in arrow_to_cardinal:
                return (i, j), arrow_to_cardinal[grid[i][j]]
    return None, None

def in_bounds(node):
    x, y = node
    return 0 <= x < n_rows and 0 <= y < n_cols

def obstruction_generator(original_grid):
    start_pos, _ = find_start(original_grid)
    n_rows = len(original_grid)
    n_cols = len(original_grid[0])
    
    for i in range(n_rows):
        for j in range(n_cols):
            if original_grid[i][j] == '.' and (i, j) != start_pos:
                modified = [row[:] for row in original_grid]
                modified[i][j] = '#'  
                yield modified

def quick_cycle(mod_grid):
    loops = 0
    position, cardinal = find_start(mod_grid)
    if position is None:
        print("No starting position found.")
        exit()
    
    visited = set()
    visited.add((position, cardinal))
    
    while True:
        dx, dy = cardinal_dict[cardinal]
        next_pos = (position[0] + dx, position[1] + dy)
        
      
        if (next_pos, cardinal) in visited:
            loops += 1 
            break

        if not in_bounds(next_pos):
            break
        
        if mod_grid[next_pos[0]][next_pos[1]] == '#':
            cardinal = rotate_right(cardinal)
            continue
        else:
            position = next_pos
            visited.add((position, cardinal))  
    
    return loops

loops = 0
for mod_grid in obstruction_generator(grid):
    print(f'Loops processed')
    loops += quick_cycle(mod_grid)
print(loops)
