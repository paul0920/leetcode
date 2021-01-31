from collections import defaultdict

numCourses = 5
prerequisites = [[1, 0], [0, 1]]

g = defaultdict(list)
visit = [0 for _ in range(numCourses)]

for course, pre in prerequisites:
    g[course].append(pre)


def dfs(course):
    if visit[course] == 1:
        return True

    if visit[course] == -1:
        return False

    # The first time seeing this course and
    # not sure whether there is a loop
    visit[course] = -1

    for pre in g[course]:

        if not dfs(pre):
            return False

    # There is no loop in this branch
    visit[course] = 1

    return True


for course in range(numCourses):

    if not dfs(course):
        print False

print True
