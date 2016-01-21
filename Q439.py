class SegmentTreeNode:
	def __init__(self, start, end, max):
		self.start, self.end, self.max = start, end, max
		self.left, self.right = None, None

class Solution:
	def build(self, A):
		return helper(self, A, 0, len(A) - 1)

	def helper(self, A, start, end):
		if start <= end:
			root = SegmentTreeNode(start, end, max(A[start : end + 1]))
			if start != end:
				mid = (start + end) // 2
				root.left = self.helper(A, start, mid)
				root.right = self.helper(A, mid + 1, end)
			return root