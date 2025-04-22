#Completed 22/04/2025#

pairs = []
with open('day-23/INPUT23.txt', 'r') as f:
    for line in f:
        line = line.strip()           # Remove trailing newline
        line = list(line.split('-'))  # Split line into components
        pairs.append(line)

node = {}
for start, end in pairs:
    if start in node:
        node[start].append(end)
    else:
        node[start] = [end]
        
    if end in node:
        node[end].append(start)
    else:
        node[end] = [start]

triangles = set()
for sub_node in node:
    neighbours = node[sub_node]
    for i in range(len(neighbours)):
        for j in range(i + 1, len(neighbours)):
            b = neighbours[i]
            c = neighbours[j]

            if b in node and c in node[b]:
                trio = sorted([sub_node, b, c])
                triangles.add(tuple(trio))

count = 0
for tri in triangles:
    for name in tri:
        if name.startswith('t'):
            count +=1
            break

print(count)


