# Time complexity: O(n log n)
import heapq


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    heap = [1]
    visited = {1}
    val = None

    for _ in range(n):
        val = heapq.heappop(heap)

        for factor in [2, 3, 5]:
            ugly_num = val * factor

            if ugly_num not in visited:
                visited.add(ugly_num)
                heapq.heappush(heap, ugly_num)

    return val


n = 10
print nthUglyNumber(n)
