
arr = []

# Need a trailing comma to indicate this is a list
arr += 'abc',
print arr

# If no trailing comma, translate 'ggg' to a list
arr += 'ccc'
print arr

arr += ['bbb']
print arr
print ""


print list('fff')
