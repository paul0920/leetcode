
p = [1, 2, 3]

def foo():

    # OK
    p.append(5)

    # OK
    p[0] = 5

    # Get error!
    # p += [5]


foo()

print p
