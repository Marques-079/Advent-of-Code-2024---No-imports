with open("day-7/INPUT7.txt") as f:
    all_text = f.read().strip()

lines = all_text.split("\n")

result = []

for line in lines:
    target, digits = line.split(":")
    target = int(target.strip())
    digits_list = list(map(int, digits.strip().split()))
    result.append([target, digits_list])

def evaluate_expression(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        else:
            result *= nums[i + 1]
    return result

def is_valid_equation(target, nums):
    num_ops = len(nums) - 1
    for i in range(2 ** num_ops):
        ops = []
        for j in range(num_ops):
            if (i >> j) & 1:
                ops.append('*')
            else:
                ops.append('+')
        if evaluate_expression(nums, ops) == target:
            return True
    return False

valid_targets = []
invalid_targets = []

for target, digits_list in result:
    if is_valid_equation(target, digits_list):
        valid_targets.append(target)
    else:
        invalid_targets.append(target)

print("Sum of valid target values:", sum(valid_targets))
