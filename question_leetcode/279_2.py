
n = 7


square_list = []
for i in range(1, n + 1):

    square_num = i ** 2

    if square_num <= n:
        square_list += [square_num]

    else:
        break

dp = [float('INF')] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for square_num in square_list:

        # Keep updating the smallest count from square_list regarding to i
        if i >= square_num:
            dp[i] = min(dp[i], dp[i - square_num] + 1)

        else:
            break

print dp[-1]
