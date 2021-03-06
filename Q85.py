class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def insertNode(self, root, node):
		if not root:
			return node
		if node.val < root.val:
			root.left = self.insertNode(root.left, node)
		else:
			root.right = self.insertNode(root.right, node)
		return root

nums = [2, 1, 4, 3]
tree = [TreeNode(n) for n in nums]
tree[0].left = tree[1]
tree[0].right = tree[2]
tree[2].left = tree[3]
root = tree[0]

node = TreeNode(6)

inst = Solution()
inst.insertNode(root, node)