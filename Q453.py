class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def flatten(self, root):
		return self.helper(root)

	def helper(self, root):
		if not root:
			return None
		if not root.left and not root.right:
			return root
		if not root.left:
			root.right = self.helper(root.right)
			return root
		if not root.right:
			root.right = self.helper(root.left)
			root.left = None
			return root
		LEFT = self.helper(root.left)
		RIGHT = self.helper(root.right)
		root.left = None
		root.right = LEFT
		node = root.right
		prev = root
		while node:
			prev = node
			node = node.right
		prev.right = RIGHT
		return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
root.right.right = TreeNode(6)

inst = Solution()
root = inst.flatten(root)

while root:
	print(root.val, end = ' ')
	root = root.right
print()