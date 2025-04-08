#Completed 08/04/2025

from collections import defaultdict
def split_even(n):
    s = str(n)
    mid = len(s) // 2
    return int(s[:mid]), int(s[mid:])

with open('day-11/INPUT11.txt', 'r') as f:
    stones = list(map(int, f.read().split()))

stone_counts = defaultdict(int)
for s in stones:
    stone_counts[s] += 1

for _ in range(75):
    new_counts = defaultdict(int)
    for value, count in stone_counts.items():
        if value == 0:
            new_counts[1] += count
        elif len(str(value)) % 2 == 0:
            left, right = split_even(value)
            new_counts[left] += count
            new_counts[right] += count
        else:
            new_counts[value * 2024] += count
    stone_counts = new_counts

print(sum(stone_counts.values()))
