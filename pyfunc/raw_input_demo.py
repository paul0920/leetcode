def c(x):
    return 4 * x


def a(y):
    return y * 1


print "Example: c(l) or a(l)"
print ""
pro = raw_input("Type a function: ")

for l in range(1, 5):
    if pro == 'c(l)':
        print "If length is", l, ", Perimeter =", eval(pro)

    elif pro == 'a(l)':
        print "If length is", l, ", Area = ", eval(pro)

    else:
        print('Wrong Function')
        break
