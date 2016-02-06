'''
Thoughts:

DFS
'''

class Solution:
	def postorderTraversal(self, root):
		self.res = []
		self.helper(root)
		return self.res

	def helper(self, root):
		if root:
			self.helper(root.left)
			self.helper(root.right)
			self.res.append(root.val)