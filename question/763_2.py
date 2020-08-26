# Time complexity: O(len(S))
import collections

S = "ababcbacadefegdehijhklij"

box = collections.defaultdict(int)
start = 0
end = 0
res = []

for idx, c in enumerate(S):
    box[c] = idx

for idx, c in enumerate(S):

    end = max(end, box[c])

    if idx == end:
        res.append(end - start + 1)
        start = end + 1

print res
