with open('day-08/INPUT8.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

def x_axis_distance_chars(chars):
    return abs(chars[0][0] - chars[1][0])
def y_axis_distance(chars):
    return abs(chars[0][1] - chars[1][1])

def grad_chars(chars):
    dx = chars[0][0] - chars[1][0]
    dy = chars[0][1] - chars[1][1]  
    if dx == 0:
        return float('-1') #Vertical inline
    elif dy == 0:
        return float('-2') #Horizontal inline
    else:
        return dy/dx  #Normal gradient exepcect +/-
    
def locate_antinodes(pair):
    grad = grad_chars(pair)
    x_axis_distance = x_axis_distance_chars(pair) #Need to toggle this (Left or right) along vector course
    y_axis_distance = y_axis_distance(pair) # Need to toggle this also (up or down) along vector course

    unbound_antiodes = []
    for i in pair:
        if grad > 0 and grad != '-1' and grad != '-2': #Postivie gradient
            backwards_coords = (i[0] - x_axis_distance, i[1] - y_axis_distance)
            forwards_coords = (i[0] + x_axis_distance, i[1] + y_axis_distance)
            if backwards_coords == pair[0] or pair[1]:
                unbound_antiodes.append(forwards_coords)
            else:
                unbound_antiodes.append(backwards_coords)

        if grad < 0 and grad != '-1' and grad != '-2': #negative gradient
            backwards_coords = (i[0] - x_axis_distance, i[1] + y_axis_distance)
            forwards_coords = (i[0] + x_axis_distance, i[1] - y_axis_distance)
            if backwards_coords == pair[0] or pair[1]:
                unbound_antiodes.append(forwards_coords)
            else:
                unbound_antiodes.append(backwards_coords)

        if grad == '-1': #Vertical inline
            distance = abs(pair[0][1] - pair[1][1])
            up_coords = (i[0], i[1]+ distance)
            down_coords = (i[0], i[1] - distance)
            if up_coords == pair[0] or pair[1]:
                unbound_antiodes.append(down_coords)
            else:
                unbound_antiodes.append(up_coords)

        if grad == '-2': #Horizontal inline
            distance = abs(pair[0][0] - pair[1][0])
            left_coords = (i[0], i[1]- distance)
            right_coords = (i[0], i[1] + distance)
            if left_coords == pair[0] or pair[1]:
                unbound_antiodes.append(right_coords)
            else:
                unbound_antiodes.append(left_coords)
           
    return unbound_antiodes

n_rows = len(grid)
n_cols = len(grid[0])

unique_chars = dict()
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] != '.':
            char = grid[i][j]
            if char not in unique_chars:
                unique_chars[char] = set()
            unique_chars[char].add((i, j))

locations_to_calc = []
locations_to_calc = []

for char in unique_chars:  # char is the key like 'A', '0', etc.
    positions = list(unique_chars[char])  # list of coordinates for that char
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            locations_to_calc.append((p1, p2))

count = 0
for pair in locations_to_calc:
    antinodes = locate_antinodes(pair)
    for antinode in antinodes:
        if  0 <= antinode[0] < n_rows and 0 <= antinode[1] < n_cols:
            count += 1
        else:
            continue
    



    
    