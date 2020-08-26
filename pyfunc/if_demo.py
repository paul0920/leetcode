
a = 2
# a = 3

def x():
    print "this is x function"
    return 4


# If a == 3, skip "or" comparison
if a == 3 or a == x():
    print "Match"

if a == 1:
    print 1

elif a == 2:
    print 2

elif a == 2:
    print 3
