'''
Thoughts:

Similar to Q69 Binary Tree Level Order Traversal, the only difference is to reverse self.res before returning it in levelOrderBottom()

'''

class Solution:
	def levelOrderBottom(self, root):
		self.res = []
		self.helper(root, 0)
		return self.res[::-1]

	def helper(self, root, level):
		if root:
			if level >= len(self.res):
				self.res.append([root.val])
			else:
				self.res[level].append(root.val)
			self.helper(root.left, level + 1)
			self.helper(root.right, level + 1)