# Completed on 31/03/2025#

with open("day-02/INPUT2.txt") as f:
    lines = f.read().strip().splitlines()

data = [list(map(int, line.strip().split())) for line in lines]

def check_safe(arr, pointer1, pointer2, ascending):
    for _ in range(len(arr) - 1):
        diff = arr[pointer2] - arr[pointer1]
        
        if not (1 <= abs(diff) <= 3):
            return False
        
        if ascending and diff <= 0:
            return False
        if not ascending and diff >= 0:
            return False

        pointer1 += 1
        pointer2 += 1

    return True

count = 0
for report in data:
    if report[0] == report[1]:
        continue  # skip flat lines
    ascending = report[0] < report[1]
    
    if check_safe(report, 0, 1, ascending):
        count += 1

print(f'Total safe reports are: {count}')


    