class segmentTreeNode:
	def __init__(self, start, end, sum):
		self.start, self.end, self.sum = start, end, sum
		self.left, self.right = None, None

class Solution:	
	
	def __init__(self, A):
		self.root = self.build(A, 0, len(A) - 1)
	
	def build(self, A, start, end):
		if start <= end:
			root = segmentTreeNode(start, end, sum(A[start : end + 1]))
			if start != end:
				mid = (start + end) // 2
				root.left = self.build(A, start, mid)
				root.right = self.build(A, mid + 1, end)
			return root
	
	def query(self, start, end):
		return self.queryHelper(self.root, start, end)
	
	def queryHelper(self, root, start, end):
		if root.start == start and root.end == end:
			return root.sum
		mid = (root.start + root.end) // 2
		if end <= mid:
			return self.queryHelper(root.left, start, end)
		if start > mid:
			return self.queryHelper(root.right, start, end)
		return self.queryHelper(root.left, start, mid) + self.queryHelper(root.right, mid + 1, end)

	def modify(self, index, value):
		oldValue = self.query(index, index)
		diff = value - oldValue
		self.modifyHelper(self.root, index, diff)
		
	def modifyHelper(self, root, index, diff):
		root.sum += diff
		if root.start != root.end:
			mid = (root.start + root.end) // 2
			if index <= mid:
				self.modifyHelper(root.left, index, diff)
			else:
				self.modifyHelper(root.right, index, diff)

A = [1, 2, 7, 8, 5]

inst = Solution(A)
print(inst.query(0, 2))
inst.modify(0, 4)
print(inst.query(0, 1))
inst.modify(2, 1)
print(inst.query(2, 4))