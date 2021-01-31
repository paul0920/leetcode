import collections

A = [1, 2, 1, 2, 3]
K = 2


def combination(diff_n):
    if diff_n < 0:
        return 0

    h_map = collections.defaultdict(int)
    start = 0
    res = 0

    for idx, n in enumerate(A):

        if not h_map[n]:
            diff_n -= 1

        h_map[n] += 1

        while diff_n < 0:

            h_map[A[start]] -= 1

            if not h_map[A[start]]:
                diff_n += 1

            start += 1

        res += idx - start + 1

    return res


print combination(K) - combination(K - 1)
