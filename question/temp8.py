import collections

grid = [[0, 0, 1],
        [1, 1, 0],
        [1, 0, 0]]
grid = [[1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]]


def show(m):
    for row in m.values():
        print row[1]

    print ""


tail_zero_count = collections.defaultdict(tuple)
step = 0

for i, row in enumerate(grid):
    for idx, num in enumerate(row[::-1]):

        if num == 1:
            tail_zero_count[i] = (idx, row)
            break

size = len(tail_zero_count)

# Apply bubble sort concept
for i in range(size):
    for j in range(i, size):

        print "i: %s, j: %s" % (i, j)
        show(tail_zero_count)

        tail_zero_count[i], tail_zero_count[j] = tail_zero_count[j], tail_zero_count[i]

        print "i: %s, j: %s" % (i, j)
        show(tail_zero_count)

        # ">" is possible solution
        if tail_zero_count[i][0] >= size - 1 - i:
            step += j - i
            print "step:", step
            print "----"
            break

    else:
        print -1
        exit()

print step
