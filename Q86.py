class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class BSTIterator:
	def __init__(self, root):
		self.stack = []
		while root:
			self.stack.append(root)
			root = root.left

	def hasNext(self):
		return self.stack

	def next(self):
		if self.stack:
			tmp = self.stack.pop()
		if tmp.right:
			root = tmp.right
			while root:
				self.stack.append(root)
				root = root.left
		return tmp

nums = [10, 1, 11, 6, 12]
tree = [TreeNode(n) for n in nums]
tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].right = tree[3]
tree[2].right = tree[4]
root = tree[0]

iterator = BSTIterator(root)
while iterator.hasNext():
	print(iterator.next().val)