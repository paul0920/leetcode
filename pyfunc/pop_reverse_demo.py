
a = list("apple")
b = list("apple")

arr = ""

while a:
    arr += a.pop()[::-1]

print arr[::-1]

arr = ""

while b:
    arr = b.pop() + arr

print arr
