'''
Thoughts:

If not root, return 0
Otherwise, return 1 plus the maximum of the maximum depth of the left and right child of root

'''
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1