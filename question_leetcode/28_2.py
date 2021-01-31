
haystack = "hello"
needle = "ll"


m = len(needle)
n = len(haystack)
power = 1
needle_code = 0
haystack_code = 0
BASE = 10 ** 6
NUM = 31

if not haystack and needle:
    print -1
    exit()

if not needle:
    print 0
    exit()

for i in range(m):
    power = (power * NUM) % BASE
    needle_code = (needle_code * NUM + ord(needle[i])) % BASE

for i in range(n):

    haystack_code = (haystack_code * NUM + ord(haystack[i])) % BASE

    if i > m - 1:
        haystack_code = haystack_code - (ord(haystack[i - m]) * power) % BASE

        # In case that some languages have different results of
        # % operation for negative numbers
        if haystack_code < 0:
            haystack_code += BASE

    if haystack_code == needle_code:

        # Need to double check since different substring may have the same hash code
        for j in range(m):

            idx = i - m + 1
            if haystack[idx + j] != needle[j]:
                break

        # Here is the a for/else loop
        else:
            print idx
            exit()

print -1
