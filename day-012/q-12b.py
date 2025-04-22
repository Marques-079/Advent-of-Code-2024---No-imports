#Completed 10/04/2025 

with open('day-12/INPUT12.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

seen = set()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_letters = {(0, 1): '>', (1, 0): 'V', (0, -1): '<', (-1, 0): '^'}

def in_bounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def dfs(x, y, typ):
    
    seen.add((x, y, typ))
    area = 1
    perimeter = 0
    edge_list = []
    
    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = cx + dx, cy + dy
        
            if not in_bounds(new_x, new_y):
                perimeter += 1
                edge_list.append((cx, cy, direction_letters[(dx, dy)]))
            
            elif grid[new_x][new_y] != typ:
                perimeter += 1
                edge_list.append((cx, cy, direction_letters[(dx, dy)]))
            
            elif (new_x, new_y, typ) not in seen:
                seen.add((new_x, new_y, typ))
                area += 1 
                queue.append((new_x, new_y))
    return area, perimeter, edge_list


def group_consecutive(nums):
    if not nums:
        return []
    
    nums = sorted(nums)  # Ensure it's sorted
    groups = []
    current_group = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_group.append(nums[i])
        else:
            groups.append(current_group)
            current_group = [nums[i]]
    
    groups.append(current_group)  # Add the last group
    return groups


def count_edges(points):
  
    sliced = []
    sliced2 = []
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    total = 0
    #Cycled though horizontal edges (Up and down)
    for i in range(min_x, max_x + 1):  
        for j in points:
            if i == j[0] and j[2] == '^':
                sliced.append(j[1])
            elif i == j[0] and j[2] == 'V':
                sliced2.append(j[1])
        #print(sliced)
        #print(sliced2)
        total += len(group_consecutive(sliced))
        total += len(group_consecutive(sliced2))
        sliced = []
        sliced2 = []
        
    # Now we need to do this for the vertical edges (Left and right)
    for i in range(min_y, max_y + 1):  
        for j in points:
            if i == j[1] and j[2] == '<':
                sliced.append(j[0])
            elif i == j[1] and j[2] == '>':
                sliced2.append(j[0])
        #print(sliced)
        #print(sliced2)
        total += len(group_consecutive(sliced))
        total += len(group_consecutive(sliced2))
        sliced = []
        sliced2 = []

    return total

value = 0
bfs_edges_collection = []
areas = []
perimeters = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        cell_type = grid[i][j]
        if (i, j, cell_type) not in seen:
            a, p, edges = dfs(i, j, cell_type)
            value += a * p
            areas.append(a)
            bfs_edges_collection.append(((i, j), edges))

for i in range(len(bfs_edges_collection)):
    perimeters.append(count_edges(bfs_edges_collection[i][1]))

totalsums = sum(a * b for a, b in zip(areas, perimeters))
print(totalsums)

