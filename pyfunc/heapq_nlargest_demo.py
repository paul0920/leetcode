import heapq

a = [0, 1, 2, 3, 4, 5]
print a[-4:]
print ""

print heapq.nlargest(4, a)
print heapq.nsmallest(4, a)
