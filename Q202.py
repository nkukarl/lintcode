class SegmentTreeNode:
	def __init__(self, start, end, max):
		self.start, self.end, self.max = start, end, max
		self.left, self.right = None, None

class Solution:	
	def query(self, root, start, end):
		if start <= end:
			if root.start == start and root.end == end:
				return root.max
			mid = (root.start + root.end) // 2
			if end <= mid:
				return self.query(root.left, start, end)
			if start > mid:
				return self.query(root.right, start, end)
			return max(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))