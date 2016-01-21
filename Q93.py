class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
			return False
		return self.isBalanced(root.left) and self.isBalanced(root.right)

	def getDepth(self, root):
		if not root:
			return 0
		else:
			return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

nums = [3, 9, 20, 15, 7]
tree = [TreeNode(n) for n in nums]
tree[0].left = tree[1]
tree[0].right = tree[2]
tree[2].left = tree[3]
tree[2].right = tree[4]

root = tree[0]

inst = Solution()
print(inst.isBalanced(root))
