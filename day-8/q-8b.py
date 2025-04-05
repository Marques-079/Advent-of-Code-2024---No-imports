def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def parse_grid(input_str):
    grid = input_str.strip().splitlines()
    antennas_by_freq = {}
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char != '.':
                if char not in antennas_by_freq:
                    antennas_by_freq[char] = []
                antennas_by_freq[char].append((r, c))
    return grid, antennas_by_freq

def mark_line_points(point, dr, dc, rows, cols):
    points = set()
    r, c = point
    while 0 <= r < rows and 0 <= c < cols:
        points.add((r, c))
        r += dr
        c += dc
    r, c = point
    while 0 <= r < rows and 0 <= c < cols:
        points.add((r, c))
        r -= dr
        c -= dc
    return points

def solve(input_str):
    grid, antennas_by_freq = parse_grid(input_str)
    rows = len(grid)
    cols = len(grid[0])
    antinode_positions = set()
    for freq, positions in antennas_by_freq.items():
        if len(positions) < 2:
            continue
        seen_lines = set()
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1 = positions[i]
                p2 = positions[j]
                dr = p2[0] - p1[0]
                dc = p2[1] - p1[1]
                g = gcd(dr, dc)
                if g != 0:
                    dr //= g
                    dc //= g
                cross = p1[0] * dc - p1[1] * dr
                line_id = (dr, dc, cross)
                if line_id in seen_lines:
                    continue
                seen_lines.add(line_id)
                line_points = mark_line_points(p1, dr, dc, rows, cols)
                antinode_positions.update(line_points)
    return len(antinode_positions)

if __name__ == '__main__':
    with open('day-8/INPUT8.txt', 'r') as f:
        input_str = f.read()
    print("Antinode count:", solve(input_str))
