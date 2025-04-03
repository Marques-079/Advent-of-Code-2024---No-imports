from collections import deque, defaultdict

pair_data = []
list_data = []

with open('day-5/INPUT5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            pair_data.append(line)
        elif ',' in line:
            list_data.append(line)

rules = defaultdict(set)
#anti_rules = defaultdict(set)

for pair in pair_data:
    left, right = pair.split('|')
    a = int(left)
    b = int(right)
    rules[a].add(b)  #A must come before B - Lookup for A precencse 
    #anti_rules[b].add(a)   #A must come before B  - Lookup for B precencse 

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
    
    # Build graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize in-degree to 0 for every page in this update
    for p in pages:
        in_degree[p] = 0

    # Populate graph edges for the relevant rules
    for a in pages:
        if a in rules:
            for b in rules[a]:
                if b in pages:
                    # a -> b
                    graph[a].append(b)
                    in_degree[b] += 1

    # Start queue with nodes that have in_degree = 0
    queue = deque([p for p in pages if in_degree[p] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) == len(pages):
        return list(sorted_order)
    else:
        # There's a cycle or contradiction
        return None
    
print(invalid_updates)
sorted_invalids = []

for i in invalid_updates:
    sorted_invalids.append(topological_sort(i, rules))

total_sum = 0
for pages in sorted_invalids:
    n = len(pages)
    middle_idx = n // 2
    middle_page = pages[middle_idx]
    total_sum += middle_page

print("Sum of the middle pages of all invalid updates:", total_sum)

