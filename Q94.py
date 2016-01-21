class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def maxPathSum(self, root):
		if not root:
			return 0
		return self.helper(root)[1]

	def helper(self, root):
		if not root:
			return 0
		l, r = 0, 0
		ls, rs = None, None
		if root.left:
			l, ls = self.helper(root.left)
			l = max(l, 0)
		if root.right:
			r, rs = self.helper(root.right)
			r = max(r, 0)
		return root.val + max(l, r), max(root.val + l + r, ls, rs)