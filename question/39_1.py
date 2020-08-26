
# candidates = [2, 3, 6, 7]
# target = 7

candidates = [2, 3, 5]
target = 8

res = []
box = []
res_set = []

def backtrack(res, box, total_num, target):
    if total_num > target:
        return

    if total_num == target:
        res.append(sorted(box))

    for i in candidates:
        backtrack(res, box + [i], total_num + i, target)


backtrack(res, [], 0, target)

for i, arr in enumerate(res):

    if not arr in res_set:
        res_set.append(arr)

print res_set
