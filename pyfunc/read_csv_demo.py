import csv
import numpy as np

with open("/Users/pochia/Downloads/numpy_test.csv") as file_csv:
    reader = csv.reader(file_csv)
    data = [[float(char) for char in row] for row in list(reader)]

for row in data:
    print row
print ""

array_list = []
for line in open("/Users/pochia/Downloads/numpy_test.csv"):
    line = line.rstrip()  # Strip the \n from each line
    row = line.split(",")
    array_list.append([float(char) for char in row])

for row in array_list:
    print row
print ""

matrix = np.genfromtxt("/Users/pochia/Downloads/numpy_test.csv", dtype=None, delimiter=",")

print matrix
print ""
print matrix * 100
print ""

output = np.arange(10).reshape(5, 2)
print output
