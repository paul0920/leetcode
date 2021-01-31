
words = ["abcd", "dcba", "lls", "s", "sssll"]


res = []

def isPalindrome(word):
    i = 0
    j = len(word) - 1

    while i < j:

        if word[i] != word[j]:
            return False

        i += 1
        j -= 1

    return True


for i in range(len(words)):
    for j in range(len(words)):

        if i != j and isPalindrome(words[i] + words[j]):
            res.append([i, j])

print res
