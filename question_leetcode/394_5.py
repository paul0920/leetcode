def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    stack = []

    for char in s:
        if char.isdigit():
            stack.append(char)

        elif char == "[":
            string = ""

            while stack and stack[-1].isdigit():  # handle the case that number > 9 (2 digits and above)
                string += stack.pop()

            stack.append(int("".join(string[::-1])))
            stack.append("[")

        elif char == "]":
            string = ""

            while stack and stack[-1] != "[":
                if stack[-1].isdigit():
                    string = string * stack.pop()
                    continue

                string += stack.pop()[::-1]  # remember to reverse the word

            stack.pop()  # remove "["
            stack.append(string[::-1] * stack.pop())  # remember to reverse the word

        else:
            stack.append(char)  # Remember to merge all elements in the stack

    return "".join(stack)


s = "2[2[y]pq4[2[jk]e1[f]]]"
print decodeString(s)
