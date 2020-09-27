
def cal_1(a, b):
    print "This is a callback"
    return a * b


def cal_2(a, b):
    print "This is a callback"
    return a - b


def get_res(cal_fun, x, y):
    return cal_fun(x, y)


print get_res(cal_1, 2, 8)
print get_res(cal_2, 2, 8)
