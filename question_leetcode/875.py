def minEatingSpeed(piles, H):
    """
    :type piles: List[int]
    :type H: int
    :rtype: int
    """
    if not piles:
        return 0

    left = 1
    right = max(piles)

    # Get the first position of the target
    while left + 1 < right:

        mid = left + (right - left) // 2

        # get_hours(left) > H >= get_hours(right)
        if get_hours(mid, piles) > H:  # Put "mid" instead of "left" into get_hours()
            left = mid

        else:
            right = mid

    if get_hours(left, piles) <= H:
        return left

    if get_hours(right, piles) <= H:
        return right


def get_hours(banana_per_hour, piles):
    count = 0

    for banana in piles:
        eating_rate = banana / banana_per_hour
        count += eating_rate if banana % banana_per_hour == 0 else eating_rate + 1

    return count


piles = [3, 6, 7, 11]
H = 8

piles = [1000]
H = 999

piles = [999]
H = 1000

print minEatingSpeed(piles, H)
