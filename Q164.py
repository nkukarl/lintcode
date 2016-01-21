class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def generateTrees(self, n):
		return self.helper(1, n + 1)
		
	def helper(self, left, right):
		res = []
		if left >= right:
			return [None]
		for i in range(left, right):
			leftTrees = self.helper(left, i)
			rightTrees = self.helper(i + 1, right)
			for lt in leftTrees:
				for rt in rightTrees:
					root = TreeNode(i)
					root.left = lt
					root.right = rt
					res.append(root)
		return res

inst = Solution()
inst.generateTrees(3)