with open("day-13/INPUT13.txt") as f:
    text = f.read()

def get_info(text):
    machines = []
    blocks = text.strip().split("\n\n")
    
    for block in blocks:
        lines = block.strip().split("\n")

        a_line = lines[0]
        b_line = lines[1]
        p_line = lines[2]
        
        ax_start = a_line.index("X+") + 2
        ax_end = a_line.index(",", ax_start)
        ax = int(a_line[ax_start:ax_end])

        ay_start = a_line.index("Y+") + 2
        ay = int(a_line[ay_start:])

        bx_start = b_line.index("X+") + 2
        bx_end = b_line.index(",", bx_start)
        bx = int(b_line[bx_start:bx_end])

        by_start = b_line.index("Y+") + 2
        by = int(b_line[by_start:])

        px_start = p_line.index("X=") + 2
        px_end = p_line.index(",", px_start)
        px = int(p_line[px_start:px_end])

        py_start = p_line.index("Y=") + 2
        py = int(p_line[py_start:])

        machines.append({
            "A": (ax, ay),
            "B": (bx, by),
            "P": (px, py)
        })

    return machines

def find_calc(ax, ay, bx, by, px, py): #py and px are target positions
    best_cost = float("inf")
    best_a, best_b = None, None

    for i in range(0, 101):
        x_room = px - (i * ax) #I is the number of A movements needed
        y_room = py - (i * ay)

        if bx == 0 or by == 0:
            continue

        if x_room % bx != 0 or y_room % by != 0:
            continue

        x_calc = x_room // bx #Number of B momvements needed 
        y_calc = y_room // by

        if x_calc == y_calc: #Both agree on same number of B button presses#
            cost = 3 * i + x_calc
            if cost < best_cost:
                best_cost = cost
                best_a, best_b = i, x_calc
    return best_cost if best_a is not None and best_b is not None else None

sum = 0
select = get_info(text)
for machine in select:

    ax, ay = machine["A"]
    bx, by = machine["B"]
    px, py = machine["P"]

    cost = find_calc(ax, ay, bx, by, px, py)
    if cost is not None:
        sum += cost
print(sum)

