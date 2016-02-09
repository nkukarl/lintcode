class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

'''
Thoughts:

Initialise an empty stack, self.stack = []
Run pushLeft() to iteratively push the left of current root to self.stack

As long as self.stack is not empty, the tree would not have been traversed, hence hasNext() simply return self.stack

next() shall return the top item of self.stack
However, if the top item of self.stack has right child, apply pushLeft() to the right child


'''

class BSTIterator:
	def __init__(self, root):
		self.stack = []
		self.pushLeft(root)

	def hasNext(self):
		return self.stack

	def next(self):
		tmp = self.stack.pop()
		if tmp.right:
			self.pushLeft(tmp.right)
		return tmp

	def pushLeft(self, root):
		while root:
			self.stack.append(root)
			root = root.left

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