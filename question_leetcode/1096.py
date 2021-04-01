def braceExpansionII(expression):
    """
    :type expression: str
    :rtype: List[str]
    """
    stack = []
    chars = []
    next_chars = []

    for _, char in enumerate(expression):
        if char == "{":
            stack.append(chars)
            stack.append(next_chars)
            chars, next_chars = [], []

        elif char.isalpha():
            curr_stack = []

            if not next_chars:
                curr_stack.append(char)

            # {ab, z}
            #  ^ next_chars
            #   ^ char
            else:
                for item in next_chars:
                    curr_stack.append(item + char)

            next_chars = curr_stack

        elif char == ",":
            chars += next_chars
            next_chars = []

        elif char == "}":
            pre_next_chars, pre_chars = stack.pop(), stack.pop()
            curr_all_chars = chars + next_chars
            curr_stack = []

            # {c, {d, e}}
            # pre_chars = [c], chars = [d], next_chars = [e]
            # -> chars = [c], next_chars = [d, e]
            if not pre_next_chars:
                for item in curr_all_chars:
                    curr_stack.append(item)

            # {a,b}{c,{d,e}}
            # pre_chars = [], pre_next_chars = [a, b], chars = [c], next_chars = [d, e]
            # -> chars = [], next_chars = [ac, ad, ae, bc, bd, be]
            else:
                for pre_item in pre_next_chars:
                    for item in curr_all_chars:
                        curr_stack.append(pre_item + item)

            next_chars = curr_stack
            chars = pre_chars

        # print stack, chars, next_chars

    return sorted(set(next_chars))


expression = "{a,b}{c,{d,e}}"
print braceExpansionII(expression)
