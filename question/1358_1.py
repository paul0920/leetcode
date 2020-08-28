import collections

s = "aaacb"


def combination(diff_n):
    h_map = collections.defaultdict(int)
    res = 0
    start = 0
    count = 0

    for idx, c in enumerate(s):

        if not h_map[c]:
            count += 1

        h_map[c] += 1

        while count > diff_n:

            h_map[s[start]] -= 1

            if not h_map[s[start]]:
                count -= 1

            start += 1

        res += idx - start + 1

    return res


print combination(3) - combination(2)
