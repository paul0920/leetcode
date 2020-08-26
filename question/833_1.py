
S = "vmokgggqzp"
indexes = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]

S = "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
indexes = [46, 29, 2, 44, 31, 26, 42, 9, 38, 23, 36, 12, 16, 7, 33, 18]
sources = ["rym", "kv", "nbzxu", "vx", "js", "tp", "tc", "jta", "zqm", "ya", "uz", "avm", "tz", "wn", "yv", "ird"]
targets = ["gfhc", "uq", "dntkw", "wql", "s", "dmp", "jqi", "fp", "hs", "aqz", "ix", "jag", "n", "l", "y", "zww"]


mdf_s = []
arr = []
i = 0
j = 0

for idx, s_idx in enumerate(indexes):
    arr.append((s_idx, sources[idx], targets[idx]))

arr.sort()

while i < len(S):

    mdf_s += S[i]

    # print mdf_s

    if j < len(indexes) and i == arr[j][0]:

        if S[i:i + len(arr[j][1])] == arr[j][1]:
            mdf_s.pop()
            mdf_s += list(arr[j][2])
            i += len(arr[j][1]) - 1

        j += 1

    i += 1

print "".join(mdf_s)
