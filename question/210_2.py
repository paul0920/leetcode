from collections import defaultdict

numCourses = 5
prerequisites = [[1, 0], [0, 1]]
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]


g = defaultdict(list)
visit = [0 for _ in range(numCourses)]
res = []

for course, pre in prerequisites:
    g[course].append(pre)

# print g

def dfs(course):
    # The first time seeing this course and
    # not sure whether there is a loop
    visit[course] = -1
    print course

    for pre in g[course]:

        if visit[pre] < 0 or (visit[pre] == 0 and not dfs(pre)):
            return False

    # There is no loop in this branch
    visit[course] = 1
    res.append(course)

    return True


for course in range(numCourses):

    if not visit[course] and not dfs(course):
        print []
        exit()

print res
