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


def v_out():
    for i in itertools.count():
        for v in v1, v2:
            if i < len(v):
                yield v[i]


gen = v_out()

for item in gen:
    print item

print "END"
