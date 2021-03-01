def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates and target != 0:
        return []

    res = []
    candidates.sort()
    subsets(candidates, target, 0, 0, [], res)

    return res


def subsets(candidates, target, index, prev_sum, path, res):
    if prev_sum > target:
        return

    if prev_sum == target:
        res.append(list(path))

        return

    for i in range(index, len(candidates)):
        if i > index and candidates[i - 1] == candidates[i]:
            continue

        num = candidates[i]
        path.append(num)
        subsets(candidates, target, i + 1, prev_sum + num, path, res)
        path.pop()


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print combinationSum2(candidates, target)
