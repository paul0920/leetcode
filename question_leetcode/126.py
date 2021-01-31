import collections

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# wordList = ["hot", "dot", "dog", "lot", "log", "cog", "cot"]


hash_w_list = set(wordList)
layer = {beginWord: [[beginWord]]}

if not endWord in hash_w_list:
    print []

while layer:

    next_layer = collections.defaultdict(list)

    for word in layer:

        if word == endWord:
            print layer[word]
            exit()

        else:

            for idx in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:idx] + c + word[idx + 1:]

                    if next_word in hash_w_list:
                        next_layer[next_word] += [ladder + [next_word] for ladder in layer[word]]

                        # print word, next_word
                        # print next_layer
                        # print ""

    hash_w_list -= set(next_layer.keys())
    layer = next_layer

print []
