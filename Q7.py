class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def serialize(self, root):
		if not root:
			return []
		self.depth = self.getDepth(root)
		self.res = [[] for _ in range(self.depth)]
		self.helper(root, 0)
		data = []
		for r in self.res:
			data += r
		return data

	def helper(self, root, level):
		if level >= self.depth:
			return
		if root:
			self.res[level].append(root.val)
			self.helper(root.left, level + 1)
			self.helper(root.right, level + 1)
		else:
			self.res[level].append('#')

	def getDepth(self, root):
		if not root:
			return 0
		return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

	def deserialize(self, data):
		if not data:
			return
		tree = []
		for n in data:
			if n != '#':
				tree.append(TreeNode(n))
			else:
				tree.append(None)

		i, j = 0, 1
		while j < len(data):
			if tree[i]:
				tree[i].left = tree[j]
				j += 1
				if j < len(data):
					tree[i].right = tree[j]
					j += 1
			i += 1

		return tree[0]


data = [3, 9, 20, '#', '#', 15, 7, 4, '#', 11, 8]

data = [1, '#', 2]

inst = Solution()

root = inst.deserialize(data)

print(inst.getDepth(root))
print(inst.serialize(root))