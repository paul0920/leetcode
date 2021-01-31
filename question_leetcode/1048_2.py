
words = ["a", "b", "ba", "bca", "bda", "bdca"]

ans = 0
words_set = set(words)
dp = {}

def dfs(word):
    if word in dp:
        return dp[word]

    ans = 1

    for i in range(len(word)):
        next_word = word[:i] + word[i + 1:]
        print word, "-->", next_word, "?"

        if next_word in words_set:
            ans = max(1 + dfs(next_word), ans)
            print word, "-->", next_word, ans

    dp[word] = ans
    print word, dp
    print ""

    return ans


for word in words:
    ans = max(ans, dfs(word))

print ans
