
A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]


# for d in zip(A, B):
#     print set(d)
#
# print ""


# print reduce(set.__or__, (set(d) for d in zip(A, B)))
s = reduce(set.__and__, (set(d) for d in zip(A, B)))

if not s:
    print -1
    exit()

x = s.pop()

print min(len(A) - A.count(x), len(B) - B.count(x))
