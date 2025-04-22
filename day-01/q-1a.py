#Solved 29/03/2025

with open("day-01/INPUT.txt") as f:
    lines = f.read().strip().splitlines()

left = []
right = []

for line in lines:
    l, r = map(int, line.strip().split())
    left.append(l)
    right.append(r)

def sort_data(data):
    data.sort()
    return data

def compare_lists(list1, list2):
    diff_total = []
    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        diff_total.append(diff)
    diff_total = sum(diff_total)
    return diff_total

list1 = sort_data(left)
list2 = sort_data(right)

diff_total = compare_lists(list1, list2)
print(f'This is the list mismatch: {diff_total}')



