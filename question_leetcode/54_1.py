
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [2, 4, 6]]

matrix_demo = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [2, 4, 6]]


def show(m):
    for row in m:
        print row


res = []
c = 0

while matrix and c < 10:

    show(matrix_demo)
    print ""
    show(matrix)

    res += matrix.pop(0)
    print "res:", res

    matrix_demo = zip(*matrix_demo)
    matrix_demo.reverse()

    matrix = zip(*matrix)
    matrix.reverse()
    c += 1

    print ""

print res
