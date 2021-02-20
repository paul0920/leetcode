# TLE due to permutation time complexity: O(n!)

def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if not s1:
        return True

    if s1 and not s2:
        return False

    visited = [False] * len(s1)
    permutations = set()
    dfs(sorted(list(s1)), [], visited, permutations)

    for i in range(len(s2) - len(s1) + 1):
        if tuple(s2[i: i + len(s1)]) in permutations:
            return True

    return False


def dfs(s, path, visited, permutations):
    if len(s) == len(path):
        permutations.add(tuple(path))

    for i in range(len(s)):
        if visited[i]:
            continue

        if i > 0 and s[i - 1] == s[i] and not visited[i - 1]:
            continue

        visited[i] = True
        path.append(s[i])
        dfs(s, path, visited, permutations)
        path.pop()
        visited[i] = False


s1 = "ab"
s2 = "eidbaooo"
s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"
print checkInclusion(s1, s2)
