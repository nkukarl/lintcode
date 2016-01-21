class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def minDepth(self, root):
		if not root:
			return 0
		if not root.left and not root.right:
			return 1
		if not root.left:
			return self.minDepth(root.right) + 1
		if not root.right:
			return self.minDepth(root.left) + 1
		return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

inst = Solution()
print(inst.minDepth(root))