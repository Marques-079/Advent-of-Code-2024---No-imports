#Completed 22/04/2025#

secret_numbers = []
with open('day-22/INPUT22.txt', 'r') as f:
    for line in f:
        secret_numbers.append(int(line))

def iterate(secret, i):
    for _ in range(i):
        mix1 = (secret ^ (secret * 64)) % 16777216
        mix2 = (mix1 ^ (mix1 // 32)) % 16777216
        mix3 = (mix2 ^ (mix2 * 2048)) % 16777216

        secret = mix3

    return mix3

total = 0
for secret in secret_numbers:
    total += iterate(secret, 2000)
print(total)
