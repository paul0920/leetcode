matrix = [[1,10,4,2],[9,18,8,7],[15,16,17,12]]

mi = [min(row) for row in matrix]

# zip(*zippedList) is a great function to extract columns in 2D matrix
# It returns an iterator of tuples with each tuple having elements from all the iterables.
mx = [max(col) for col in zip(*matrix)]
mx_col = [col for col in zip(*matrix)]

print mx_col

for i in mi:
    if i in mx:
        print i