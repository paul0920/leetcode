import itertools

A = [37, 12, 28, 9, 100, 56, 80, 5, 12]

# itertools.count is infinite iterators [Arguments: start, [step]; Results: start, start+step, start+2*step, ...]
print zip(A, itertools.count(1))