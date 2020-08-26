import itertools

v1 = [1, 2]
v2 = [3, 4, 5, 6]

for a in itertools.count():
    if a > 10:
        break

    else:
        print a

print "END"
print ""

res = []

for i in itertools.count():
    for v in (v1, v2):
        if i < len(v):
            res.append(v[i])
            print res, i, v

    if len(res) == (len(v1) + len(v2)):

        break

print ""

# itertools.count() keeps running since there is no break
# it can only be used in the tuple instead of list
vl = ((v[i], i, v) for i in itertools.count() for v in (v1, v2) if i < len(v))

# vl is not working
vl = [(v[i], i, v) for i in itertools.count() for v in (v1, v2) if i < len(v)]

print vl
print next(vl)
print next(vl)
print next(vl)
print next(vl)
print next(vl)
print next(vl), "5"

# since itertools.count() keep running and this code won't stop
print next(vl), "6"
