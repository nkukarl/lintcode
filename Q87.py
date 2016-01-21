class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def removeNode(self, root, value):
		if not root:
			return
		if root.val == value:
			if root.right:
				tmp = root.right
				while tmp.left:
					tmp = tmp.left
				tmp.left = root.left
				return root.right
			return root.left
		if root.val < value:
			root.right = self.removeNode(root.right, value)
		else:
			root.left = self.removeNode(root.left, value)
		return root

nums = [5, 3, 6, 2, 4]
tree = [TreeNode(n) for n in nums]

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].left = tree[3]
tree[1].right = tree[4]
root = tree[0]

value = 1

inst = Solution()
newRoot = inst.removeNode(root, value)