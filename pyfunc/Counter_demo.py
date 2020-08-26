import collections

secret = "1211"
guess = "2221"

s = collections.Counter(secret)
g = collections.Counter(guess)


print s
print g
print s & g

# Counter works like a hash table and returns an array
print (s & g).keys()
print (s & g).values()
print (s & g).items()
