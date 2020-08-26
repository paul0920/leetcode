
S = "heeellooo"
words = ["hello", "hi", "helo"]

S = "abbbc"
words = ["abbc"]


def check(S, W):

    i, j, n, m = 0, 0, len(S), len(W)

    for i in range(n):

        print i, j
        # print S[i], W[j]
        print S[i - 1:i + 2]
        print S[i] * 3
        print S[i - 2:i + 1]

        if j < m and S[i] == W[j]:
            j += 1

        elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]:
            print "WRONG"
            print ""
            return False

        print "*******"

    # print j, m
    return j == m


print sum(check(S, W) for W in words)
