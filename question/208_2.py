
class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.isWord = False

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: None
		"""
		for c in word:
			self = self.children.setdefault(c, Trie())

		self.isWord = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""

		if not self.children:
			return self.isWord

		for c in word:
			if c in self.children:
				self = self.children[c]

			else:
				return False

		return self.isWord

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""

		if not self.children:
			return self.isWord

		for c in prefix:
			if c in self.children:
				self = self.children[c]

			else:
				return False

		return True
		# return self


trie_tree = Trie()
trie_tree.insert("bluebird")

print trie_tree.search("bluebird")
print trie_tree.startsWith("bl")
