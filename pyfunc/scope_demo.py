# JavaScript also has the following scope and IIFE concept,
# which are similar to Python

def my_func_a(i):
    print i

def my_func_b():
    # i = 3.14
    print i

def closure(m):

    def my_func_c():
        print m

    return my_func_c


arr2 = []
arr = []

for i in range(2):

    arr2 += [my_func_a]
    arr += [my_func_b]

# print arr2
# print arr

# i = 100
print "the 1st i: ", i
arr2[0](1234)
arr[0]()
print ""

i = 200
print "the 2nd i: ", i
arr2[1](4321)
arr[1]()
print ""

# my_func_b searches i nearby
for j in range(2):
    arr[j]()
print ""

# IIFE
print (lambda i: i + 2)(123)
print ""


arr1 = []

for i in range(2):
    arr1 += [closure(i)]

for q in range(2):
    arr1[q]()
