
S = "abbaba"
# S = "abbbba"


# print S[:-1]

ans = 0
for i in range(1, len(S)):

    if ans >= len(S) - i:
        break

    tmp = 0
    for x, y in zip(S[i:], S[:-i]):

        # print x, y

        if x == y:
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0

print ans
