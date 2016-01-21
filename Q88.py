class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def lowestCommonAncestor(self, root, A, B):
		if A == root or B == root:
			return root
		if self.isSubTree(root.left, A) and self.isSubTree(root.left, B):
			return self.lowestCommonAncestor(root.left, A, B)
		if self.isSubTree(root.right, A) and self.isSubTree(root.right, B):
			return self.lowestCommonAncestor(root.right, A, B)
		return root

	def isSubTree(self, root, node):
		if not node:
			return True
		if not root:
			return False
		if root == node:
			return True
		return self.isSubTree(root.left, node) or self.isSubTree(root.right, node)


nums = [4, 3, 7, 5, 6]
tree = [TreeNode(n) for n in nums]
tree[0].left = tree[1]
tree[1].right = tree[2]
tree[2].left = tree[3]
tree[2].right = tree[4]

root = tree[0]

inst = Solution()
lca = inst.lowestCommonAncestor(root, tree[2], tree[1])

print(lca.val)
