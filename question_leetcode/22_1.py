
# The boundary function should be:
# number of '(' <= n
# number of ')' <= number of '('
# Time complexity: O(2 ^ (2n + 1))

n = 3
res = []

def backtrack(res, pair, open, close, n):

    # Check whether it gets all the combinations
    if len(pair) == 2 * n:
        res.append(pair)
        return

    # Keep going if open < n
    if open < n:
        backtrack(res, pair + '(', open + 1, close, n)

    # Start closing the (
    if close < open:
        backtrack(res, pair + ')', open, close + 1, n)


backtrack(res, '', 0, 0, n)

print res
