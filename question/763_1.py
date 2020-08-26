# Time complexity: O(len(S)^2)

S = "ababcbacadefegdehijhklij"

res = []

while S:
    idx = 1

    while set(S[:idx]) & set(S[idx:]):
        idx += 1

    res.append(idx)
    S = S[idx:]

print res
