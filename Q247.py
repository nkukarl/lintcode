class SegmentTreeNode:
	def __init__(self, start, end, count):
		self.start, self.end, self.count = start, end, count
		self.left, self.right = None, None

class Solution:
	def query(self, root, start, end):
		if not root:
			return 0
		start = max(start, root.start)
		end = min(end, root.end)
		if root.start == start and root.end == end:
			return root.count
		mid = (root.start + root.end) // 2
		if end <= mid:
			return self.query(root.left, start, end)
		if start > mid:
			return self.query(root.right, start, end)
		return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)