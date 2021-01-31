import collections

S = "abbaba"


h_map = collections.defaultdict(int)

for i in range(len(S)):
    for j in range(i, len(S)):

        # print S[i:j+1]

        h_map[S[i:j + 1]] += 1

# print h_map

print max([len(word) for word, times in h_map.items() if times > 1] + [0])
