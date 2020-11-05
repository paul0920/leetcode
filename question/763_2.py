# Time complexity: O(len(S))

S = "ababcbacadefegdehijhklij"


lookup_table = {}
start = 0
end = 0
res = []

for i, c in enumerate(S):
    lookup_table[c] = i

for i, c in enumerate(S):

    end = max(end, lookup_table[c])

    if end == i:
        res += [end - start + 1]
        start = end + 1

print res
