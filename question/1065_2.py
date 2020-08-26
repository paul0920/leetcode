
text = "thestoryofleetcodeandme"
words = ["story", "fleet", "leetcode"]

class TrieNode:

    def __init__(self):
        self.children, self.is_word = {}, False

    def construct_trie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node.children.setdefault(c, TrieNode())
                node = node.children[c]
            node.is_word = True
        return root


obj = TrieNode()
root = obj.construct_trie(words)
# trie = TrieNode.construct_trie(words)

res = []

for l in range(len(text)):
    node = root
    for r in range(l, len(text)):
        if text[r] not in node.children:
            break
        node = node.children[text[r]]
        if node.is_word:
            res.append((l, r))

print res
