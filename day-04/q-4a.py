#Completed 31/03/2025#

with open("day-04/INPUT4.txt") as f:
    lines = f.read().strip().splitlines()

def horizontal_check(line):
    horiz_sum = 0
    for i in range(len(line)- 3):
        if line[i:i+4] == 'XMAS':
            horiz_sum += 1
    return horiz_sum

def vertical_check(four_set):
    vert_sum = 0
    for i in range(len(four_set[0]) - 3):
        if (four_set[0][i] == 'X' and
            four_set[1][i] == 'M' and
            four_set[2][i] == 'A' and
            four_set[3][i] == 'S'):
            vert_sum += 1
    return vert_sum


def diagonal_check_right(four_set):
    diag_sum_right = 0
    for i in range(len(four_set[0]) - 3):
        if (four_set[0][i] == 'X' and
            four_set[1][i+1] == 'M' and
            four_set[2][i+2] == 'A' and
            four_set[3][i+3] == 'S'):
            diag_sum_right += 1
    return diag_sum_right


def diagonal_check_left(four_set):
    diag_sum_left = 0
    for i in range(3, len(four_set[0])):
        if (four_set[0][i] == 'X' and
            four_set[1][i-1] == 'M' and
            four_set[2][i-2] == 'A' and
            four_set[3][i-3] == 'S'):
            diag_sum_left += 1
    return diag_sum_left

#Logic to account for backward words

def flipped_horizontal_check(line):
    horiz_sum = 0
    for i in range(len(line)-3):
        if line[i:i+4] == 'SAMX':
            horiz_sum += 1
    return horiz_sum

def flipped_vertical_check(four_set):
    vert_sum = 0
    for i in range(len(four_set[0])):
        if (four_set[0][i] == 'S' and
            four_set[1][i] == 'A' and
            four_set[2][i] == 'M' and
            four_set[3][i] == 'X'):
            vert_sum += 1
    return vert_sum


def flipped_diagonal_check_right(four_set):
    diag_sum_right = 0
    for i in range(len(four_set[0]) - 3):
        if (four_set[0][i] == 'S' and
            four_set[1][i+1] == 'A' and
            four_set[2][i+2] == 'M' and
            four_set[3][i+3] == 'X'):
            diag_sum_right += 1
    return diag_sum_right

def flipped_diagonal_check_left(four_set):
    diag_sum_left = 0
    for i in range(3, len(four_set[0])):
        if (four_set[0][i] == 'S' and
            four_set[1][i-1] == 'A' and
            four_set[2][i-2] == 'M' and
            four_set[3][i-3] == 'X'):
            diag_sum_left += 1
    return diag_sum_left


#Final running logic
total_sum = 0

# Horizontal scan
for line in lines:
    total_sum += horizontal_check(line)
    total_sum += flipped_horizontal_check(line)

# Vertical & diagonal scan
for i in range(len(lines) - 3): 
    segment = lines[i:i+4] 
    total_sum += vertical_check(segment)
    total_sum += diagonal_check_right(segment)
    total_sum += diagonal_check_left(segment)

# Flipped scans
    total_sum += flipped_vertical_check(segment)
    total_sum += flipped_diagonal_check_right(segment)
    total_sum += flipped_diagonal_check_left(segment)

print(f'Total sum of XMAS: {total_sum}')

            



    
    
            


