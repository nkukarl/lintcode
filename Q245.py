class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None

class Solution:
	def isSubtree(self, T1, T2):
		if not T2:
			return True
		if not T1:
			return False
		if self.isSametree(T1, T2):
			return True
		return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

	def isSametree(self, T1, T2):
		if not T1 and not T2:
			return True
		if not T1 or not T2:
			return False
		if T1.val != T2.val:
			return False
		return self.isSametree(T1.left, T2.left) and self.isSametree(T1.right, T2.right)