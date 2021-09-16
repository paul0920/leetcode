def addOperators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if not num:
        return []

    res = []

    for i in range(len(num)):
        curr_num = int(num[: i + 1])
        dfs(i + 1, num, target, curr_num, curr_num, [str(curr_num)], res)

        if curr_num == 0:
            break

    return res


def dfs(index, num, target, pre_num, total_sum, path, res):
    if index == len(num):
        if total_sum != target:
            return

        res.append("".join(path))

        return

    for i in range(index, len(num)):
        curr_num = int(num[index: i + 1])
        dfs(i + 1, num, target, curr_num, total_sum + curr_num, path + ["+", str(curr_num)], res)
        dfs(i + 1, num, target, -curr_num, total_sum - curr_num, path + ["-", str(curr_num)], res)
        dfs(i + 1, num, target, pre_num * curr_num, total_sum - pre_num + pre_num * curr_num,
            path + ["*", str(curr_num)], res)

        if curr_num == 0:
            break


num = "105"
target = 5
print addOperators(num, target)
