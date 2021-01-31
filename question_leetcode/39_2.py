
# candidates = [2, 3, 6, 7]
# target = 7

candidates = [2, 3, 5]
target = 8

candidates.sort()
res = []

def backtrack(idx, path, left):

    # print idx, path, left

    if not left:
        res.append(path)

    # This is an important condition about pointing to
    # the right index, Otherwise, there are many repeating combinations
    for i, v in enumerate(candidates[idx:], idx):

        if v > left:
            return

        backtrack(i, path + [v], left - v)


backtrack(0, [], target)

print res
