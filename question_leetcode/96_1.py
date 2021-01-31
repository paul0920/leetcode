# DP (Bottom Up)

# n = 19
n = 3

state = [0] * (n + 1)
state[0] = 1

# Calculate each n state
for n1 in range(1, n + 1):
    # Sweep different root in each n state
    for root in range(1, n1 + 1):
        state[n1] += state[root - 1] * state[n1 - root]

print state[n]
