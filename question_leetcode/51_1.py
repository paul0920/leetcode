# Time complexity: O(s * n^2), s = solution counts

def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    if not n:
        return []

    cols = []
    res = []
    search(n, cols, res)

    return res


def search(n, cols, res):
    # Start with row index in 0
    row = len(cols)

    if row == n:
        res.append(create_board(cols))
        return

    for col in range(n):
        if not is_valid(row, col, cols):
            continue

        # Do DFS
        cols.append(col)
        search(n, cols, res)
        cols.pop()


def is_valid(row, col, cols):
    for r, c in enumerate(cols):
        if c == col:
            return False

        # Check whether (r, c) and (row, col) are on the same 2 diagonals
        if r - c == row - col or r + c == row + col:
            return False

    return True


def create_board(cols):
    n = len(cols)
    res = []

    for i in range(n):
        curr_row = []

        for j in range(n):
            if j == cols[i]:
                curr_row.append("Q")

            else:
                curr_row.append(".")

        res.append("".join(curr_row))

    return res


n = 4
print solveNQueens(n)
