# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object
# such as a list, dictionary, or instances of most classes.


def f(a, l=[]):
    l.append(a)

    return l


def g(a, l=None):
    if l is None:
        l = []

    l.append(a)

    return l


print f(1)
print f(2)
print f(3)
print f.__defaults__
print ""
print g(1)
print g(2)
print g(3)
print g.__defaults__
