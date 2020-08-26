
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

print order.index('z')

f = lambda x: map(order.index, x)

print f("app")
print f("apple")
print f("app") < f("apple")

words.sort(key=f)

print words
