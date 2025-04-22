#Completed 08/04/2025

with open('day-11/INPUT11.txt', 'r') as f:
    lines = f.read().split()  
lines = [int(x) for x in lines]

def one_rep(lines):
    new_list = []
    for i in lines:
        if i == 0:
            new_list.append(1)
        elif len(str(i)) % 2 == 0:
            s = str(i)
            mid = len(s) // 2
            left = int(s[:mid])
            right = int(s[mid:])
            new_list.extend([left, right])
        else:
            new_list.append(i * 2024)
    return new_list

for _ in range(25):
    lines = one_rep(lines)

print(len(lines))
