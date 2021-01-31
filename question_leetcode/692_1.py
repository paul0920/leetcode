import collections

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4


word_count = collections.Counter(words)

res = []

for each_word in sorted(word_count, key=lambda x: (-word_count[x], x)):

    res.append(each_word)

    if len(res) == k:
        break

print res
