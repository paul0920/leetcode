
# raw_input() takes exactly what the user typed and passes it back as a string.
# input() first takes the raw_input() and then performs an eval() on it as well.

def c(l):
  return 4*l

def a(l):
  return l*1

print "Example: c(4)"
print ""
property = input("Type a function: ")

print property