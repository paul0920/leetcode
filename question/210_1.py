
numCourses = 5
prerequisites = [[1, 0], [0, 2], [2, 1], [3, 4]]
# numCourses = 1
# prerequisites = []

src, dst = [set() for _ in range(numCourses)], [set() for _ in range(numCourses)]

for d, s in prerequisites:
    src[d].add(s), dst[s].add(d)

# Start with the courses with no any prerequisites
ans = [x for x in range(numCourses) if not src[x]]

for s in ans:
    for d in dst[s]:

        src[d].remove(s)
        # This course, d, doesn't have any prerequisites
        if not src[d]:
            ans.append(d)

print ans if len(ans) == numCourses else []
