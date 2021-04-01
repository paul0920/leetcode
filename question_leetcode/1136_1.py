# Time complexity: O(n + m), m = len(relations) (edges)

import collections


def minimumSemesters(n, relations):
    """
    :type n: int
    :type relations: List[List[int]]
    :rtype: int
    """
    if not relations:
        return 1

    pre_to_current = {i: set() for i in range(1, n + 1)}
    current_to_pre = {i: set() for i in range(1, n + 1)}

    for pre_course, course in relations:
        pre_to_current[pre_course].add(course)
        current_to_pre[course].add(pre_course)

    queue = collections.deque()

    for i in range(1, n + 1):
        if current_to_pre[i]:
            continue

        queue.append(i)

    total_non_pre_course = len(queue)
    res = 0

    while queue:
        for _ in range(len(queue)):
            course = queue.popleft()

            for next_course in pre_to_current[course]:
                current_to_pre[next_course].remove(course)

                if not len(current_to_pre[next_course]):
                    total_non_pre_course += 1
                    # Remember to add the node into the queue!
                    queue.append(next_course)

        res += 1

    return res if total_non_pre_course == n else -1


n = 3
relations = [[1, 3], [2, 3]]
print minimumSemesters(n, relations)
