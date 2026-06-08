# fig1_lfsr.py

def lfsr(seed, taps, length):
    sr = seed[:]  # shift register as a list of bits
    output = []
    for _ in range(length):
        # XOR the tap positions
        feedback = 0
        for t in taps:
            feedback ^= sr[t]
        output.append(sr[-1])  # output is the last bit
        sr = [feedback] + sr[:-1]  # shift right, insert feedback at start
    return output

# Example usage
# Seed: initial bits, Taps: positions used for XOR
seed = [1, 0, 0, 1, 1]   # 5-bit seed
taps = [0, 2]            # XOR positions
length = 20              # number of bits to generate

sequence = lfsr(seed, taps, length)

print("Seed:", seed)
print("Taps:", taps)
print("Generated Sequence:", sequence)
