# Return the identity of an object.  This is guaranteed to be unique among
# simultaneously existing objects.  (Hint: it's the object's memory address.)

a = [1, 2, 3]
b = a
c = a[:]

print id(a) - id(a)
print id(b) - id(a)
print id(c) - id(a)
