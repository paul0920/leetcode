import collections

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

word_pool = set(wordList)
q = collections.deque()
q.append((beginWord, 1))

while q:

    word, count = q.popleft()

    if word == endWord:
        print count
        exit()

    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':

            next_word = word[:i] + c + word[i + 1:]

            if next_word in word_pool:
                q.append((next_word, count + 1))
                word_pool.remove(next_word)

print 0
