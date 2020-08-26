import collections

hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
hand = [1, 2, 6, 2, 4, 7, 8]
W = 3


count = collections.Counter(hand)

for n in sorted(count):

    if count[n] > 0:

        for i in range(W)[::-1]:

            count[n + i] -= count[n]

            if count[n + i] < 0:
                print False
                exit()

print True
