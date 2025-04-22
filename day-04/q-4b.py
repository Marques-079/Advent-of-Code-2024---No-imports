#Completed 31/03/2025

def pattern1(grid):
    if (grid[0][0] == 'M' and
        grid[0][2] =='M' and
        grid[1][1] == 'A' and
        grid [2][0] == 'S' and
        grid[2][2] == 'S'):
        return True
    
    elif (grid[0][0] == 'S' and
        grid[0][2] =='M' and
        grid[1][1] == 'A' and
        grid [2][0] == 'S' and
        grid[2][2] == 'M'):
        return True
    
    elif (grid[0][0] == 'S' and
        grid[0][2] =='S' and
        grid[1][1] == 'A' and
        grid [2][0] == 'M' and
        grid[2][2] == 'M'):
        return True
    
    elif (grid[0][0] == 'M' and
        grid[0][2] =='S' and
        grid[1][1] == 'A' and
        grid [2][0] == 'M' and
        grid[2][2] == 'S'):
        return True
    else:
        return False
    
with open("day-04/INPUT4.txt") as f:
    lines = f.read().strip().splitlines()

total = 0
for j in range(len(lines)-2):
    for i in range(len(lines[0])-2):
        grid = [
            lines[j][i:i+3],
            lines[j+1][i:i+3],
            lines[j+2][i:i+3]
        ]
        if pattern1(grid):
            total += 1

print(total)
