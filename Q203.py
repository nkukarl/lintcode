class SegmentTreeNode:
	def __init__(self, start, end, max):
		self.start, self.end, self.max = start, end, max
		self.left, self.right = None, None

class Solution:
	def modify(self, root, index, value):
		if root.start == root.end:
			root.max = value
		else:
			mid = (root.start + root.end) // 2
			if index <= mid:
				self.modify(root.left, index, value)
			else:
				self.modify(root.right, index, value)
			root.max = max(root.left.max, root.right.max)
