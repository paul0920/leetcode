import itertools

v1 = [1, 2]
v2 = [3, 40, 5, 6]


def v_out_a():

    for i in range(10):
        for v in v1, v2:
            if i < len(v):
                yield v[i]

def v_out_b():

    # This itertools.count() won't stop and keep running...
    for i in itertools.count():
        # print i
        for v in v1, v2:
            if i < len(v):
                yield v[i]


gen = v_out_a()

for n in gen:
    print n

print "******"

gen = v_out_b()

# This won't stop due to itertools.count() & next()
for _ in range(7):
    print next(gen), "this is outcome"

print "******"
