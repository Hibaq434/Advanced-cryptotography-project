# fig2_lfsr_output.py

def lfsr(seed, taps, length):
    sr = seed[:]  # shift register
    output = []
    for _ in range(length):
        feedback = 0
        for t in taps:
            feedback ^= sr[t]
        output.append(sr[-1])  # output bit
        sr = [feedback] + sr[:-1]
    return output

# Example usage
seed = [1, 0, 0, 1, 1]   # 5-bit seed
taps = [0, 2]            # XOR positions
length = 32              # generate 32 bits

sequence = lfsr(seed, taps, length)

# Format output as grouped bits
grouped = ''.join(str(bit) for bit in sequence)
print("Seed:", seed)
print("Taps:", taps)
print("Generated Sequence (32 bits):")
print(grouped)

# Show sequence grouped in 8-bit chunks
print("\nGrouped as bytes:")
for i in range(0, len(grouped), 8):
    print(grouped[i:i+8])
