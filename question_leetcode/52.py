def totalNQueens(n):
    """
    :type n: int
    :rtype: int
    """
    if not n:
        return 0

    count = [0]
    cols = []
    visited = {
        "col": set(),
        "sum": set(),
        "diff": set()
    }

    dfs(n, cols, visited, count)

    return count[-1]


def dfs(n, cols, visited, count):
    row = len(cols)

    if row == n:
        count[-1] += 1

        return

    for col in range(n):

        if not is_valid(row, col, visited):
            continue

        cols.append(col)
        visited["col"].add(col)
        visited["sum"].add(row + col)
        visited["diff"].add(row - col)
        dfs(n, cols, visited, count)
        visited["col"].remove(col)
        visited["sum"].remove(row + col)
        visited["diff"].remove(row - col)
        cols.pop()


def is_valid(row, col, visited):
    if col in visited["col"]:
        return False

    if row + col in visited["sum"]:
        return False

    if row - col in visited["diff"]:
        return False

    return True


n = 4
print totalNQueens(n)
