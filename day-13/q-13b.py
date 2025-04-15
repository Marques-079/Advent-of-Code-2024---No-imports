#Bit of a break, completed 16/04/2025

f = open("day-13/INPUT13.txt", "r")
text = f.read()

#Target // GCD(a,b) must be True else cannot solve diophantic equation
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b): #A linear equation ax + bx = c has an integer solution if and only if g divides c.
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

#Extract all the stuff from machines and put it into a list of dictionaries
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

def solve_machine(ax, ay, bx, by, px, py):
    g = gcd(ax, bx)
    if px % g != 0:
        return None
    g, x0, y0 = extended_gcd(ax, bx)
    scale = px // g
    a0 = x0 * scale
    b0 = y0 * scale
    # a0 and b0 solve: ax * a0 + bx * b0 = px.
    # General solution: a = a0 + k * (bx/g),  b = b0 - k * (ax/g)
    sum0 = ay * a0 + by * b0
    diff = ay * (bx // g) - by * (ax // g)

    #IF diff = 0 then any Y value (in equation Y) could yeild a valid A or B but we dont know which so must sovle to optimise
    if diff == 0:
        if sum0 != py:
            return None
        kmin = -10**18
        kmax = 10**18

        #just makes our search more effcient by solving B - GIVEN - the minimum value of A is > 0
        if bx // g > 0:
            kmin = max(kmin, -a0 // (bx // g))
        elif bx // g < 0:
            kmax = min(kmax, -a0 // (bx // g))
        if (ax // g) > 0:
            kmax = min(kmax, b0 // (ax // g))
        elif (ax // g) < 0:
            kmin = max(kmin, b0 // (ax // g))
        best = None

        #Solve for the lowest a and b combo cost iterating through possible values of k
        for k in range(kmin, kmax + 1):
            a_sol = a0 + k * (bx // g)
            b_sol = b0 - k * (ax // g)
            if a_sol < 0 or b_sol < 0:
                continue

            cost = 3 * a_sol + b_sol
            if best is None or cost < best[0]:
                best = (cost, a_sol, b_sol)
        return best

    #Only a set value of K will work as solution A has to be positive and B has to be positive
    else:
        num = py - sum0
        if num % diff != 0:
            return None
        
        k = num // diff
        a_sol = a0 + k * (bx // g)
        b_sol = b0 - k * (ax // g)

        if a_sol < 0 or b_sol < 0:
            return None
        
        cost = 3 * a_sol + b_sol
        return (cost, a_sol, b_sol)

def solve_all_machines(machines):
    total_cost = 0
    wins = 0
    for m in machines:
        ax, ay = m["A"]
        bx, by = m["B"]
        px, py = m["P"]
        px += 10000000000000 #Bonuses here D:
        py += 10000000000000
        res = solve_machine(ax, ay, bx, by, px, py)
        if res is not None:
            wins += 1
            total_cost += res[0]
    return wins, total_cost

machines = get_info(text)
wins, total_cost = solve_all_machines(machines)
print(wins, total_cost)

'''
1) Check if a solution is even possible for the X movement.
We calculate the greatest common divisor (GCD) of the two X movements (from buttons A and B).
If the prize's X position isn't divisible by that GCD, it's impossible to reach — so we stop there.

2) Find one starting solution for the X direction.
We use something called the extended GCD to find a particular combination of A and B button presses that gets us to that X position (though not necessarily the Y position yet).
List all ways to reach that X position.

3) Once we have one valid (A, B) pair that reaches the prize’s X, we can use a formula to get every other possible (A, B) pair that also works for the X coordinate by varying an integer k.
Plug that into the Y direction.
We take our general formula for all X solutions and plug it into the Y equation to see which value(s) of k also make the Y coordinate match the prize.

4) Solve for k
If plugging in the general solution gives us a clean answer for k, we compute it.
If it doesn't divide nicely, there’s no way to hit both X and Y at the same time — so we skip this machine.

5) If any k works (i.e. special case), search for the best one.
Sometimes, any value of k satisfies the Y condition. In that case, we search through possible values of k that keep both A and B button presses nonnegative.

6) We look for the one with the lowest total cost (since A costs 3 tokens and B costs 1).
Reject negative button presses.

7) We only keep solutions where you don’t press buttons a negative number of times.
Calculate the total token cost.


'''
