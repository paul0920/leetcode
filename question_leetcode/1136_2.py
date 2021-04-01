# Time complexity: O(n^2), n = # of course

def minimumSemesters(n, relations):
    """
    :type n: int
    :type relations: List[List[int]]
    :rtype: int
    """
    if not relations:
        return 1

    pre_to_current = {i: set() for i in range(1, n + 1)}

    for pre_course, course in relations:
        pre_to_current[pre_course].add(course)

    dp = [0] * (n + 1)
    leaf = []

    # Initialize dp array and look for leaf node
    for pre_course, course_list, in pre_to_current.items():
        if not course_list:
            dp[pre_course] = 1
            leaf.append(pre_course)

    if not leaf:
        return -1

    for course in range(1, n + 1):
        # Reset "visited" every time while staring an new path search
        visited = set()
        dfs(course, visited, pre_to_current, dp)

        for node in visited:
            # Check whether there is any loop on the path
            # such as [1, 2], [2, 1], [2, 3]
            if dp[node] > n:
                return -1

    return max(dp)


def dfs(course, visited, pre_to_current, dp):
    visited.add(course)

    for next_course in pre_to_current[course]:
        if next_course not in visited:
            dfs(next_course, visited, pre_to_current, dp)

        # DP state function
        dp[course] = max(dp[course], dp[next_course] + 1)


n = 3
relations = [[1, 2], [2, 3], [3, 1]]
print minimumSemesters(n, relations)
