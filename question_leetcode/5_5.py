
s = "baabaad"
s = "aacabdkacaa"
# s = "cbbd"


if not s:
    print ""
    exit()

str_size = len(s)
is_palindrome = [[False] * str_size for _ in range(str_size)]
for i in range(str_size):

    is_palindrome[i][i] = True

    if i > 0:
        is_palindrome[i][i - 1] = True

start = 0
max_len = 1

# The following order is incorrect since DP has to
# start with the smallest window_size building the table!
#
# for window_size in range(str_size, 1, -1):
#
for window_size in range(2, str_size + 1):
    for i in range(str_size - window_size + 1):

        j = i + window_size - 1
        is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

        if is_palindrome[i][j] and window_size > max_len:
            max_len = window_size
            start = i

print s[start: start + max_len]
