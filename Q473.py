class TrieNode:
	def __init__(self):
		self.isWord = False
		self.leaves = dict()

class WordDictionary:
	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word):
		node = self.root
		for w in word:
			if w not in node.leaves:
				node.leaves[w] = TrieNode()
			node = node.leaves[w]
		node.isWord = True

	def search(self, word):
		return self.helper(self.root, word)

	def helper(self, root, word):
		if not word:
			return root.isWord
		if word[0] == '.':
			for leave in root.leaves:
				if self.helper(root.leaves[leave], word[1:]):
					return True
		else:
			if word[0] in root.leaves:
				return self.helper(root.leaves[word[0]], word[1:])
		return False
		

inst = WordDictionary()

inst.addWord('bad')
inst.addWord('dad')
inst.addWord('mad')

print(inst.search('ba.'))