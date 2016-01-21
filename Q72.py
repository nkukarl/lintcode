class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def buildTree(self, inorder, postorder):
		if postorder:
			val = postorder[-1]
			root = TreeNode(val)
			pos = inorder.index(val)
			root.left = self.buildTree(inorder[:pos], postorder[:pos])
			root.right = self.buildTree(inorder[pos + 1:], postorder[pos: -1])
			return root

inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

inst = Solution()
root = inst.buildTree(inorder, postorder)