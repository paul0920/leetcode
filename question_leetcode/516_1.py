
# s = "baabaad"
# s = "aacabdkacaa"
# s = "bbcddb"
s = "bcduxd"


if not s:
    print 0
    exit()

str_size = len(s)
is_subseq = [[0] * str_size for _ in range(str_size)]

for window_size in range(1, str_size + 1):
    for i in range(str_size - window_size + 1):

        j = i + window_size - 1

        if i == j:
            is_subseq[i][j] = 1

        # 2 counts for s[i] and s[j]
        elif s[i] == s[j]:
            is_subseq[i][j] = is_subseq[i + 1][j - 1] + 2

        else:
            is_subseq[i][j] = max(is_subseq[i + 1][j], is_subseq[i][j - 1])

print is_subseq[0][-1]
