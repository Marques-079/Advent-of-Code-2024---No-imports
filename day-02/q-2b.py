# Completed on 31/03/2025 - Runs in 0(n^2) time complexity D:

def spots_safe(arr):
    diffs = [arr[i+1] - arr[i] for i in range(len(arr) - 1)]

    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False

    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        return True

    return False

def safe_with_dampener(arr):
    if spots_safe(arr):
        return True
    
    for i in range(len(arr)):
        shortened = arr[:i] + arr[i+1:]
        if len(shortened) >= 2 and spots_safe(shortened):
            return True
        #Think of it like if one bad value taints the array, if we remove that bad value the array will be fine so for 1 mistake there will be 1 good array (mistake rmeoved)
        #But if there are 2 bad values present then even if we remove one through slicing one bad value will exist in the 'subset' and for the loop it will have no good values.

    return False


with open("day-02/INPUT2.txt") as f:
    lines = f.read().strip().splitlines()

data = [list(map(int, line.strip().split())) for line in lines]

safe_count = sum(1 for report in data if safe_with_dampener(report))
print(f"Total safe reports with dampener: {safe_count}")


    