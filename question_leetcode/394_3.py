def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    stack = []
    string = ""
    number = 0

    for char in s:
        if char == "[":
            stack.append((string, number))
            string = ""
            number = 0

        elif char == "]":
            pre_string, pre_number = stack.pop()
            string = pre_string + pre_number * string

        elif char.isdigit():
            number = number * 10 + int(char)

        else:
            string += char

    return string


s = "3[a]2[bc]"
print decodeString(s)
