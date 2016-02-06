'''
Thoughts:

DFS
'''

class Solution:
	def inorderTraversal(self, root):
		self.res = []
		self.helper(root)
		return self.res

	def helper(self, root):
		if root:
			self.helper(root.left)
			self.res.append(root.val)
			self.helper(root.right)