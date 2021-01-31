
text = "thestoryofleetcodeandme"
words = ["story", "fleet", "leetcode"]


class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.isWord = False


res = []

# Remember to have "()" after TrieNode
root = TrieNode()

for w in words:
    node = root

    for c in w:
        # node.children.setdefault returns node.children[c],
        # which is the next node of TrieNode
        node = node.children.setdefault(c, TrieNode())

    node.isWord = True

for i in range(len(text)):
    node = root

    for j in range(i, len(text)):

        if text[j] in node.children:
            node = node.children[text[j]]

        else:
            break

        if node.isWord:
            res.append([i, j])

print res
