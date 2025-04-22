#Compared to hard coded grid logic this is a bit shorter and cleaner

def pattern1(grid):
    diag1 = grid[0][0] + grid[1][1] + grid[2][2]
    diag2 = grid[2][0] + grid[1][1] + grid[0][2]
    return diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}

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
