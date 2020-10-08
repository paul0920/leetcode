
# Check if object is int or float: isinstance()


stack = [1, 2, 3, "+", 4, 5]

while isinstance(stack[-1], int):
    print stack.pop()
