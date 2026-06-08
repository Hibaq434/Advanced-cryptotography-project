# fig3_randomness.py

def lfsr(seed, taps, length):
    sr = seed[:]
    output = []
    for _ in range(length):
        feedback = 0
        for t in taps:
            feedback ^= sr[t]
        output.append(sr[-1])
        sr = [feedback] + sr[:-1]
    return output

# Example usage
seed = [1, 0, 0, 1, 1]
taps = [0, 2]
length = 100  # generate 100 bits

sequence = lfsr(seed, taps, length)

# Randomness testing
zeros = sequence.count(0)
ones = sequence.count(1)

print("Generated Sequence (first 32 bits):", ''.join(str(b) for b in sequence[:32]))
print("Total bits:", length)
print("Zeros:", zeros)
print("Ones:", ones)

# Balance check
balance = abs(zeros - ones)
print("Balance (difference between zeros and ones):", balance)

# Frequency ratio
print("Zero ratio:", zeros/length)
print("One ratio:", ones/length)
