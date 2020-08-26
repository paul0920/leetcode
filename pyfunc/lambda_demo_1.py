
my_list = [1, 5, 4, 6]

print map(lambda x: x * 2, my_list)

print (lambda x: x * 2)(my_list)
print my_list * 2


# A lambda function is an expression, it can be named
add_one = lambda x: x + 1
print add_one(5)

say_hi =  lambda: "hi"
print say_hi()
