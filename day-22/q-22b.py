#Completed 22/04/2025

secret_numbers = []
with open('day-22/INPUT22.txt', 'r') as f:
    for line in f:
        secret_numbers.append(int(line))


sequence_to_price = {}

def iterate(secret, i):
    prices = [secret % 10]
    for _ in range(i):
        mix1 = (secret ^ (secret * 64)) % 16777216
        mix2 = (mix1 ^ (mix1 // 32)) % 16777216
        mix3 = (mix2 ^ (mix2 * 2048)) % 16777216
        prices.append(mix3 % 10)
        secret = mix3

    return prices

def price_changes(price):
    intra_banana = []
    left  = 0
    right = 1
    while right < len(price):
        difference = price[right] - price[left] 
        intra_banana.append(difference)
        left +=1 
        right +=1
    return intra_banana
                  
def window(prices, changes):
    seen = set()
    for i in range(len(changes) - 3): 
        seq = tuple(changes[i:i+4])
        if seq in seen:
            continue 
        elif seq not in sequence_to_price:
            sequence_to_price[seq] = [prices[i + 4]]    
            seen.add(seq)
        else:
            sequence_to_price[seq].append(prices[i + 4])
            seen.add(seq)

    return sequence_to_price


def tally(sequence_to_price):
    best = 0
    for key in sequence_to_price:
        total = sum(sequence_to_price[key])
        best = max(total, best)
          
    return best
        
for secret in secret_numbers:
    prices = iterate(secret, 2000)
    changes = price_changes(prices)
    windows = window(prices, changes)
print(tally(sequence_to_price))





