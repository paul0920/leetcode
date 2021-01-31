# Recursion (Top Down) using LRU cache

# import functools
from lru_cache import *


@lru_cache()
def numTrees(n):
    if n <= 1:
        return 1

    res = 0
    for root in range(0, n):
        # numTrees(left) x numTrees(right)
        res += numTrees(root) * numTrees(n - 1 - root)

    return res


n = 19
# n = 3

print numTrees(n)
