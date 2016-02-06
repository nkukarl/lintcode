'''
Thoughts:

DFS
'''

class Solution:
	def preorderTraversal(self, root):
		self.res = []
		self.helper(root)
		return self.res

	def helper(self, root):
		if root:
			self.res.append(root.val)
			self.helper(root.left)
			self.helper(root.right)