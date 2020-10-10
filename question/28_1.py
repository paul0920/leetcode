
haystack = "hello"
needle = "ll"


n = len(haystack)
m = len(needle)

for i in range(n - m + 1):
    for j in range(m):

        if haystack[i + j] != needle[j]:
            break

    # Here is the a for/else loop
    else:
        print i
        exit()

print -1
