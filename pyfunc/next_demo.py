# next(iterable, default)
# iterable (required): an iterable object
# default (optional): an default value to return if the iterable has reached to its end

bucket = [[0, 1], [1, 10], [2, 20], [3, 30]]

key = 3
item = next((item for item in bucket if item[0] == key), None)

print item


key = 5
item = next((item for item in bucket if item[0] == key), "no such value")

print item
