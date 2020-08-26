
logs = ["dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"]

def f(log):

    # string.split(separator, maxsplit)
    idx, rest = log.split(" ", 1)

    return (0, rest, idx) if rest[0].isalpha() else (1, )


print sorted(logs, key=f)
