class segmentTreeNode:
	def __init__(self, start, end, sum):
		self.start, self.end, self.sum = start, end, sum
		self.left, self.right = None, None

class Interval:
	def __init__(self, start, end):
		self.start, self.end = start, end

class Solution:
	def intervalSum(self, A, queries):
		self.A = A
		root = self.build(0, len(A) - 1)
		res = []
		for q in queries:
			res += [self.query(root, q.start, q.end)]
		return res

	def build(self, start, end):
		if start <= end:
			root = segmentTreeNode(start, end, sum(self.A[start : end + 1]))
			if start != end:
				mid = (start + end) // 2
				root.left = self.build(start, mid)
				root.right = self.build(mid + 1, end)
			return root

	def query(self, root, start, end):
		if root.start == start and root.end == end:
			return root.sum
		mid = (root.start + root.end) // 2
		if end <= mid:
			return self.query(root.left, start, end)
		if start > mid:
			return self.query(root.right, start, end)
		return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)

A = [1, 2, 7, 8, 5]
queries = [Interval(1, 2), Interval(0, 4), Interval(2, 4)]

inst = Solution()
print(inst.intervalSum(A, queries))