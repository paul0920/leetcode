import collections

nums = [1, 2, 3, 4, 4]
nums = [1, 2, 3, 3, 4, 4, 5, 5]
# nums = [1, 2, 3, 3, 4, 4]


def show(c):
    for k, v in sorted(c.items()):
        print k, v


start = collections.Counter(nums)
end = collections.Counter()

for n in nums:

    if start[n]:

        start[n] -= 1

        # if end has the number of n - 1, append n to the sequence
        if end[n - 1] > 0:

            end[n - 1] -= 1
            end[n] += 1

        # if n + 1 and n + 2 exist in start hash map, create a new sequence
        # by adding it to the end array
        elif start[n + 1] and start[n + 2]:

            start[n + 1] -= 1
            start[n + 2] -= 1
            end[n + 2] += 1

        else:
            print False
            print "!!!!!!!!!"

        print "start:"
        show(start)
        print "end:"
        show(end)
        print "-"

print True
