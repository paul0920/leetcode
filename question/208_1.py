import collections

class Trie(object):

	def __init__(self):
		self.children = collections.defaultdict(Trie)
		self.is_word_end = False

	def insert(self, word):

		if not word:
			self.is_word_end = True
		else:
			self.children[word[0]].insert(word[1:])

	def search(self, word):

		if not word:
			return self.is_word_end
		if word[0] in self.children:
			return self.children[word[0]].search(word[1:])

		return False

	def startsWith(self, prefix):

		if not prefix:
			return True
		if prefix[0] in self.children:
			return self.children[prefix[0]].startsWith(prefix[1:])

		return False


trie_tree = Trie()
trie_tree.insert("bluebird")

print trie_tree.search("bluebird")
print trie_tree.startsWith("bl")
