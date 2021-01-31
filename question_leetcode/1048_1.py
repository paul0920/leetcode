import collections

words = ["a", "b", "ba", "bca", "bda", "bdca"]

box = collections.defaultdict(int)

for w in sorted(words, key=len):

    stack = []
    for i in range(len(w)):
        stack.append(box[w[:i] + w[i + 1:]] + 1)

    box[w] = max(stack)
    print stack
    print box
    print ""

print max(box.values())
