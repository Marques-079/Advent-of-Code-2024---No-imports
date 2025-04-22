def read_input(file_path):
    with open(file_path) as f:
        lines = f.read().strip().split('\n')
    result = []
    for line in lines:
        if ':' not in line:
            continue  # Skip bad lines
        target_str, digits_str = line.split(':')
        try:
            target = int(target_str.strip())
            digits = list(map(int, digits_str.strip().split()))
            result.append([target, digits])
        except ValueError:
            print(f"Skipping bad line: {line}")
    return result

data = read_input("day-07/INPUT7.txt")
total = 0
valid_equations = []

def evaluate_expression(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        op = ops[i]
        next_num = nums[i + 1]
        if op == '+':
            result += next_num
        elif op == '*':
            result *= next_num
        elif op == '||':
            result = int(str(result) + str(next_num))
    return result

def is_valid_equation(target, nums):
    def backtrack(index, ops):
        if index == len(nums) - 1:
            result = evaluate_expression(nums, ops)
            return result == target
        for op in ['+', '*', '||']:
            ops.append(op)
            if backtrack(index + 1, ops):
                return True
            ops.pop()
        return False

    return backtrack(0, [])



for target, digits in data:
    if is_valid_equation(target, digits):
        total += target
        valid_equations.append((target, digits))

print("Total calibration result:", total)
