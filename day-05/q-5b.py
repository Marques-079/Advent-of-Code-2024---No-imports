#Completed 03/04/2025

pair_data = []
list_data = []

with open('day-05/INPUT5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            pair_data.append(line)
        elif ',' in line:
            list_data.append(line)

rules = {}

for pair in pair_data:
    left, right = pair.split('|')
    a = int(left)
    b = int(right)

    if a not in rules:
        rules[a] = set()
    rules[a].add(b)

valid_updates = []
invalid_updates = []

for line in list_data:
    pages = list(map(int, line.split(',')))
    is_valid = True
    
    for page in pages:
        if page in rules:
            for must_come_after in rules[page]:
                if must_come_after in pages:
                    if pages.index(page) >= pages.index(must_come_after):
                        is_valid = False
                        break
        if not is_valid:
            break

    if is_valid:
        valid_updates.append(pages)
    else:
        invalid_updates.append(pages)


def topological_sort(pages, rules):
    graph = {}
    in_degree = {}

    for p in pages:
        in_degree[p] = 0
        graph[p] = []  

    for a in pages:
        if a in rules:
            for b in rules[a]:
                if b in pages:
                    # a -> b
                    graph[a].append(b)
                    in_degree[b] += 1


    queue = [p for p in pages if in_degree[p] == 0]

    sorted_order = []

    while queue:

        node = queue.pop(0)
        sorted_order.append(node)


        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
 
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) == len(pages):
        return sorted_order
    else:
        return None
        
sorted_invalids = []

for i in invalid_updates:
    sorted_result = topological_sort(i, rules)
    if sorted_result is not None:
        sorted_invalids.append(sorted_result)

total_sum = 0
for pages in sorted_invalids:
    n = len(pages)
    middle_idx = n // 2
    middle_page = pages[middle_idx]
    total_sum += middle_page    

print("Sum of the middle pages of all invalid updates:", total_sum)
