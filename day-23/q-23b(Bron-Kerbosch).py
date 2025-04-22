#Completed 22/04/2025 

node = {}
with open('day-23/INPUT23.txt') as f:
    for line in f:
        a, b = line.strip().split('-')
        node.setdefault(a, set()).add(b) 
        node.setdefault(b, set()).add(a)

'''
Makes an adjacency set similar to part A except uses sets
'''
# ─── Bron–Kerbosch with pivoting ───────────────────────────────────
best_clique = []

'''
R is the current clique we're building (every node in R is connected to every other node).
P is the set of nodes we could still try adding — they are connected to all of R.
X is the set of nodes we've already explored in other recursive paths — to prevent duplicates.

We choose a pivot from P union X — it's the node most connected to nodes in P. This helps us prune the search space.

Then, P - node[pivot] gives us the nodes that are NOT connected to the pivot. These are the nodes we try now in our loop, 
because the pivot’s neighbors will be explored from another branch.

When we select a node v from this loop:
- We add it to R
- Then update P to P ∩ node[v] (keep only nodes connected to v)
- Same for X ∩ node[v]
- This ensures we only build cliques with fully connected nodes

If P and X are both empty, we've found a maximal clique (nothing can be added to grow it). If it's larger than best_clique, we save it.

After trying v, we remove it from P and add it to X — marking it as "used", so we don't try it again later.
'''
def bronk(R, P, X):
    global best_clique
    if not P and not X:
        if len(R) > len(best_clique):
            best_clique = list(R)
        return
   
    pivot = max(P | X, key=lambda v: len(P & node[v])) if P or X else None

    for v in list(P - node[pivot]):         
        bronk(
            R | {v},
            P & node[v],
            X & node[v])
        
        P.remove(v)
        X.add(v)


all_vertices = set(node.keys())

bronk(set(), all_vertices, set())

password = ','.join(sorted(best_clique))
print(password)
'''
so we pick the most popular node in using pivot and then from the list of nodes not part of the most popular set 
we look at those first - by calling recusively on the nodes which arent part of the most popular set. 
When calling recusively the pivot may change which will free up previouslt restructed nodes which can be picked
'''