import collections


def numFriendRequests(ages):
    """
    :type ages: List[int]
    :rtype: int
    """
    if not ages:
        return 0

    age_to_count = collections.Counter(ages)
    res = 0

    for age_a in age_to_count:
        for age_b in age_to_count:
            if not is_valid_request(age_a, age_b):
                continue

            count_a = age_to_count[age_a]
            count_b = age_to_count[age_b]

            if age_a == age_b:  # C(count, 2) x 2 = count x (count - 1) for the group with the same age
                count_b -= 1

            res += count_a * count_b

    return res


def is_valid_request(a, b):
    if b <= 0.5 * a + 7:
        return False

    if b > a:
        return False

    if b > 100 and a < 100:
        return False

    return True


ages = [20, 30, 100, 110, 120]
print numFriendRequests(ages)
