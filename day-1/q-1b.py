#Solved 29/03/2025

with open("day-1/INPUT.txt") as f:
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

def similarity(list, frequency):
    total = []
    for i in range(len(list)):
        if list[i] in frequency:
            calc = list[i] * frequency[list[i]]
            total.append(calc)
        else:
            total.append(0)
        
    return sum(total)

hashed = frequency_counter(left)
similarity_total = similarity(right, hashed)
print(f'This is the similarity total: {similarity_total}')



