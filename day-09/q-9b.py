def find_free_span(disk, start_idx, end_idx, needed):

    consecutive = 0
    span_start = None
    for i in range(start_idx, end_idx + 1):
        if disk[i] == '.':
            consecutive += 1
            if consecutive == 1:
                span_start = i
            if consecutive == needed:
                return span_start
        else:
            consecutive = 0
            span_start = None
    return None

def part2_compact(disk, file_positions, max_file_id):

    for fid in range(max_file_id - 1, -1, -1):
        blocks = file_positions.get(fid, [])
        if not blocks:
            continue
        length = len(blocks)
        leftmost_block_index = min(blocks)

        if leftmost_block_index == 0:
            continue  

        span_start = find_free_span(disk, 0, leftmost_block_index - 1, length)
        if span_start is not None:

            for old_pos in blocks:
                disk[old_pos] = '.'
        
            new_positions = list(range(span_start, span_start + length))
            for pos in new_positions:
                disk[pos] = str(fid)
            file_positions[fid] = new_positions

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

file_positions = {}
for i, block in enumerate(disk):
    if block != '.':
        fid = int(block)
        if fid not in file_positions:
            file_positions[fid] = []
        file_positions[fid].append(i)

part2_compact(disk, file_positions, file_id)

checksum = 0
for pos, block in enumerate(disk):
    if block != '.':
        checksum += pos * int(block)

#print("".join(disk))  
print("Checksum:", checksum)
