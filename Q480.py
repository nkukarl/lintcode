class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def binaryTreePaths(self, root):
		if not root:
			return []
		self.res = []
		self.helper(root, [])
		return self.res

	def helper(self, root, cur):
		if not root.left and not root.right:
			final = cur + [str(root.val)]
			self.res.append('->'.join(final))
		else:
			if root.left:
				self.helper(root.left, cur + [str(root.val)])
			if root.right:
				self.helper(root.right, cur + [str(root.val)])

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)

inst = Solution()
print(inst.binaryTreePaths(root))