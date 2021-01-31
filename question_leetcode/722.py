
source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]

for row in source:
    print row
print ""

buf = ""
res = []
block_open = False

for row in source:

    i = 0

    while i < len(row):

        c = row[i]

        if c == "/" and i + 1 < len(row) and row[i + 1] == "/" and not block_open:
            i = len(row)

        elif c == "/" and i + 1 < len(row) and row[i + 1] == "*" and not block_open:
            block_open = True
            i += 1

        elif c == "*" and i + 1 < len(row) and row[i + 1] == "/" and block_open:
            block_open = False
            i += 1

        elif not block_open:
            buf += c

        i += 1

    if buf and not block_open:
        res.append(buf)
        buf = ""

for row in res:
    print row

# print res
