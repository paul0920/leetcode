
#s = "aa"
#t = "aa"

s = "cabwefgewcwaefgcf"
t = "cae"

s_map = {}

for i in t:
    s_map[i] = []

check_t = list(t)
start, end = 0, len(s)

for i in range(len(s)):

    if s[i] in t:

        if s[i] in check_t:
            check_t.remove(s[i])

        # Keep tracking the index of corresponding s[i],
        # remove the oldest index and save the newest one into the array
        elif not s[i] in check_t and s_map[s[i]] != []:
            s_map[s[i]].pop(0)

        s_map[s[i]].append(i)

    if check_t == []:

        # Find the largest or the smallest numbers in v
        max_idx = max([v[-1] for k, v in s_map.items()])
        min_idx = min([v[0] for k, v in s_map.items()])

        if max_idx - min_idx + 1 < end - start + 1:
            end = max_idx
            start = min_idx

# There is no matching window since there are items in the check_t
if check_t:
    print ""

print s[start:end + 1]