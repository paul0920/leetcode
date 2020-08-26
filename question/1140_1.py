
piles = [2, 7, 9, 4, 4]

memo = {}
total = len(piles)

# Calculate the total stone from the right to left
for i in range(total - 1, 0, -1):
    piles[i - 1] += piles[i]

# print piles

def find(curr_idx, m, piles, memo):

    if (curr_idx, m) in memo:
        return memo[(curr_idx, m)]

    # Return the max count of stone directly because everyone plays optimally
    if curr_idx + 2 * m >= total:
        # print curr_idx, m, "    ", piles[curr_idx]
        return piles[curr_idx]

    min_count = float('INF')

    # Here is the request: 1 <= X <= 2M, set M = max(M, X)
    for next_idx in range(1, 2 * m + 1):
        the_other = find(curr_idx + next_idx, max(m, next_idx), piles, memo)
        min_count = min(min_count, the_other)

    max_count = piles[curr_idx] - min_count
    memo[(curr_idx, m)] = max_count

    return max_count


print find(0, 1, piles, memo)
