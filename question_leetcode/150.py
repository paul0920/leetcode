def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    operator_set = {"+", "-", "*", "/"}

    for char in tokens:
        if stack and char in operator_set:
            num2, num1 = stack.pop(), stack.pop()

            if char == "+":
                res = num1 + num2

            if char == "-":
                res = num1 - num2

            if char == "*":
                res = num1 * num2

            if char == "/":
                # 6 / -132 = -1
                # float(6) / -132 = -0.0454545454545
                res = int(float(num1) / num2)

            stack.append(res)
            continue

        stack.append(int(char))

    return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print evalRPN(tokens)
