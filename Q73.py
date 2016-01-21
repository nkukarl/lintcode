class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def buildTree(self, preorder, inorder):
		if preorder:
			val = preorder[0]
			root = TreeNode(val)
			pos = inorder.index(val)
			root.left = self.buildTree(preorder[1 : pos + 1], inorder[:pos])
			root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
			return root

preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]

inst = Solution()
root = inst.buildTree(preorder, inorder)