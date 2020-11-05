
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
numCourses = 5
prerequisites = [[1, 0], [0, 1]]

res = []
course = [set() for _ in range(numCourses)]
pre_course = [set() for _ in range(numCourses)]

for _class, pre_class in prerequisites:
    course[_class].add(pre_class)
    pre_course[pre_class].add(_class)

res = [each_class for each_class in range(numCourses) if not course[each_class]]

for pre_class in res:
    for _class in pre_course[pre_class]:
        course[_class].remove(pre_class)

        if not course[_class]:
            res += [_class]

print res if len(res) == numCourses else []
