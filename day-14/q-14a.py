#Notes: Grid is 101 x 103 tiles#
p_v = []
with open("day-14/INPUT14.txt") as file:
    for line in file:
        parts = line.strip().split()
        
        p_str = parts[0].split('=')[1]  
        v_str = parts[1].split('=')[1] 
        
        px, py = map(int, p_str.split(','))
        vx, vy = map(int, v_str.split(','))
        
        positions = (px, py)  # Use tuple instead of list
        velocities = (vx, vy)
        
        p_v.append([positions, velocities])

def bounds(curr_position, velocity):
    x, y = curr_position
    vx, vy = velocity
    if (x + vx) > 100 or (y + vy) > 102 or (x + vx) < 0 or (y + vy) < 0:
        return False
    return True

def teleport(curr_position, velocity):
    x, y = curr_position
    vx, vy = velocity
    
    x = (x + vx) % 101  # Adjusting for grid width
    y = (y + vy) % 103  # Adjusting for grid height
    
    return x, y

def move(curr_position, velocity):
    x, y = curr_position
    vx, vy = velocity
    dx, dy = x + vx, y + vy

    if bounds((dx, dy), velocity): # If movement is contained in bounds
        return dx, dy  # Returns the new position of the bot
    else: 
        return teleport(curr_position, velocity)  # Returns the new coordinates of the bot

def simulate(p_v):
    for _ in range(100):  # Simulating for 100 seconds
        for i in range(len(p_v)):
            curr_pos = p_v[i][0]
            velocity = p_v[i][1]
            x, y = move(curr_pos, velocity)
            p_v[i][0] = (x, y)  # Update position with tuple, not list

def classify(positions):
    grid = {}  
    q1 = q2 = q3 = q4 = 0

    for x, y in positions:
        if x == 50 or y == 51:
            continue 
        key = (x, y)
        if key in grid:
            grid[key] += 1
        else:
            grid[key] = 1

    for (x, y) in grid:
        count = grid[(x, y)]
        if x > 50 and y < 51:
            q1 += count
        elif x < 50 and y < 51:
            q2 += count
        elif x < 50 and y > 51:
            q3 += count
        elif x > 50 and y > 51:
            q4 += count

    return q1 * q2 * q3 * q4


simulate(p_v)
positions = [pv[0] for pv in p_v]
product = classify(positions)
print(product)



