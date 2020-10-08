
asteroids = [4, -2, -1, 1, 2]
# asteroids = [4, 1, -2]

stack = []

for rock in asteroids:

    while stack and  rock < 0 < stack[-1]:

        if abs(stack[-1]) > abs(rock):
            break

        elif abs(stack[-1]) < abs(rock):
            stack.pop()

        else:
            stack.pop()
            break

    # "while" is similar to "if"
    else:
        stack.append(rock)

print stack
