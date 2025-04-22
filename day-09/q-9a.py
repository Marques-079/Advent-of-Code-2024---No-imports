#Completed 07/04/2025

with open('day-09/INPUT9.txt', 'r') as f:
    data = f.readline().strip()
lengths = list(map(int, data))
disk = []
is_file = True
file_id = 0

for num in lengths:
    if is_file:
        disk.extend([str(file_id)] * num)
        file_id += 1
    else:
        disk.extend(['.'] * num)
    is_file = not is_file
L, R = 0, len(disk) - 1

while L < R:
    if disk[L] != '.':
        L += 1
        continue
    if disk[R] == '.':
        R -= 1
        continue

    disk[L], disk[R] = disk[R], disk[L]
    L += 1
    R -= 1

print(''.join(disk))
checksum = sum(i * int(b) for i, b in enumerate(disk) if b != '.')
print("Checksum:", checksum)
