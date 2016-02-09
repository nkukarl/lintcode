'''
Thought:

If root is None (empty tree), return True (an empty tree is a balanced tree)
Compare the depth of the left tree with the depth of the right tree, if they differ by more than 1, return False
Otherwise, only return True when both the left tree and the right tree are balanced

getDepth() returns the depth of a tree

'''

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
			return False
		return self.isBalanced(root.left) and self.isBalanced(root.right)

	def getDepth(self, root):
		if not root:
			return 0
		else:
			return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

nums = [3, 9, 20, 15, 7]
tree = [TreeNode(n) for n in nums]
tree[0].left = tree[1]
tree[0].right = tree[2]
tree[2].left = tree[3]
tree[2].right = tree[4]

root = tree[0]

inst = Solution()
print(inst.isBalanced(root))
