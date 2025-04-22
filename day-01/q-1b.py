#Solved 29/03/2025

with open("day-01/INPUT.txt") as f:
    lines = f.read().strip().splitlines()

left = []
right = []

for line in lines:
    l, r = map(int, line.strip().split())
    left.append(l)
    right.append(r)

def frequency_counter(data):
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

frequency = frequency_counter(left)
similarity_total = sum(r * frequency.get(r, 0) for r in right)
print(f'This is the similarity total: {similarity_total}')



    