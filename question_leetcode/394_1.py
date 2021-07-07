def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    stack = []

    for char in s:
        if char != "]":
            stack.append(char)
            continue

        num = ""
        string = ""

        while stack[-1] != "[":
            # Instead of using string += stack.pop()[::-1], this can prevent from reversing stack later on
            # For example, 4[ 2[jk] e 1[f] ] -> 4["jkjk", "e", "f"]
            string = stack.pop() + string

        stack.pop()

        while stack and stack[-1].isdigit():
            # Instead of using num += stack.pop(), this can prevent from reversing num later on
            num = stack.pop() + num

        stack.append(int(num) * string)

    return "".join(stack)  # Remember to merge all elements in the stack


s = "3[a]2[bc]"
s = "2[3[a]]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print decodeString(s)
