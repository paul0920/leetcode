
A = [1, 0, 1, 0, 1]
S = 2


def combination(total):

    start = 0
    res = 0

    if total < 0:
        return 0

    for idx, num in enumerate(A):

        total -= A[idx]

        # Use "while" instead of "if" to get a correct window size
        # meeting the requested constraints
        while total < 0:
            total += A[start]
            start += 1

        res += idx - start + 1

        # print idx - start + 1

    return res


print combination(S) - combination(S - 1)
