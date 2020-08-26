import collections

hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
# hand = [1, 2, 6, 2, 4, 7, 8]
# hand = [10, 11, 12, 11, 12, 13]

W = 3


curr_count = collections.Counter(hand)
stack = collections.deque()

pre_num = -1
pre_count = 0

for num in sorted(curr_count):

    # example: [10, 11, 12, 12, 12, 13, 14], [10, 11, 12, 12, 14, 15]
    if pre_count > curr_count[num] or pre_count > 0 and num > pre_num + 1:
        print False
        exit()

    print curr_count[num], pre_count

    stack.append(curr_count[num] - pre_count)
    pre_num, pre_count = num, curr_count[num]

    print pre_num, pre_count, stack

    if len(stack) == W:
        pre_count -= stack.popleft()

    print ""

print pre_count == 0
