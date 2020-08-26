
S = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print zip(indexes, sources, targets)

# Replace the string from right to left to skip the index mapping problem
for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):

    if S[i:i + len(s)] == s:

        # print i, S[:i], S[i + len(s):]

        S = S[:i] + t + S[i + len(s):]

    # print S

print S
