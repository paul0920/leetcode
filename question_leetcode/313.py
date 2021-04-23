import heapq


def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if not primes:
        return False

    heap = [1]
    seen = set()
    seen.add(1)

    for _ in range(n):
        num = heapq.heappop(heap)

        for n in primes:
            ugly_num = num * n

            if ugly_num in seen:
                continue

            seen.add(ugly_num)
            heapq.heappush(heap, ugly_num)

    return num


n = 12
primes = [2, 7, 13, 19]
print nthSuperUglyNumber(n, primes)
