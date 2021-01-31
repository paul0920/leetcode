from collections import defaultdict

numCourses = 5
prerequisites = [[1, 0], [0, 2], [1, 2]]


g = defaultdict(list)
in_degree = [0 for _ in range(numCourses)]

for course, pre in prerequisites:
    g[pre].append(course)
    in_degree[course] += 1

# Search all the courses instead of just the courses in the g array!
bfs = [i for i in range(numCourses) if not in_degree[i]]

# Start tracing prerequisites (in_degree = 0) and
# check whether the course could be prerequisite in the future
# and attach it to the bfs array and wait for processing
for pre in bfs:
    for course in g[pre]:
        in_degree[course] -= 1

        if not in_degree[course]:
            bfs.append(course)

print len(bfs) == numCourses
