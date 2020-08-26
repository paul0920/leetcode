
piles = [2, 7, 9, 4, 4]

memo = {}
total = len(piles)

def find(curr_idx, m, piles, memo):

    if (curr_idx, m) in memo:
        return memo[(curr_idx, m)]

    future_stone = sum(piles[curr_idx:])

    # print curr_idx, m, future_stone

    # Don't need to find further since no more stones.
    # However, we can set the boundary condition to
    # be curr_idx + 2 * m >= total to close recursive call earlier
    if curr_idx + m >= total:
        return future_stone

    min_count = float('INF')

    for next_idx in range(1, 2 * m + 1):
        the_other = find(curr_idx + next_idx, max(m, next_idx), piles, memo)
        min_count = min(min_count, the_other)

    max_count = future_stone - min_count
    memo[(curr_idx, m)] = max_count

    return max_count


print find(0, 1, piles, memo)
