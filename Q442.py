class TrieNode:
	def __init__(self):
		self.isWord = False
		self.leaves = {}

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for w in word:
			if w not in node.leaves:
				node.leaves[w] = TrieNode()
			node = node.leave[w]
		node.isWord = True

	def search(self, word):
		node = self.root
		for w in word:
			if w not in node.leaves:
				return False
			node = node.leaves[w]
		return node.isWord

	def startsWith(self, prefix):
		node = self.root
		for p in prefix:
			if p not in node.leaves:
				return False
			node = node.leaves[p]
		return True

