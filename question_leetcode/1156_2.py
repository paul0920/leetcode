import collections
import itertools

# text = "ababa"
text = "aaabaaa"

res = 0
count = collections.Counter(text)
mapping = []

for s, c in itertools.groupby(text):

    # Store groupby() object in a list since the previous group
    # will be no longer visible later. Check itertools_groupby_demo.py
    # for more details
    c_len = len(list(c))

    # Extend the group count by 1 and capped by the max count
    res = max(res, min(count[s], c_len + 1))
    mapping.append([s, c_len])

for i, arr in enumerate(mapping, 1):
    if i < len(mapping) - 1 and mapping[i - 1][0] == mapping[i + 1][0] and mapping[i][1] == 1:

        # Merge 2 adjacent groups, which are separated by only 1 character
        # Capped by the max count
        res = max(res, min(count[mapping[i - 1][0]], mapping[i - 1][1] + mapping[i + 1][1] + 1))

print res
