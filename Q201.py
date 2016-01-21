class SegmentTreeNode:
	def __init__(self, start, end):
		self.start, self.end = start, end
		self.left, self.right = None, None

class Solution:	
	def build(self, start, end):
		if start <= end:
			root = SegmentTreeNode(start, end)
			if start < end:
				mid = (start + end) // 2
				root.left = self.build(start, mid)
				root.right = self.build(mid + 1, end)
			return root

inst = Solution()
inst.build(0, 3)
			