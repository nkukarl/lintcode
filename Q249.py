class segmentTreeNode:
	def __init__(self, start, end, count):
		self.start, self.end, self.count = start, end, count
		self.left, self.right = None, None

class Solution:
	def countOfSmallerNumberII(self, nums):
		root = self.build(0, 10000)
		res = []
		for n in nums:
			self.modify(root, n, 1)
			if n <= 0:
				res.append(0)
			else:
				res.append(self.query(root, 0, n - 1))
		return res


	def build(self, start, end):
		if start <= end:
			root = segmentTreeNode(start, end, 0)
			if start != end:
				mid = (start + end) // 2
				root.left = self.build(start, mid)
				root.right = self.build(mid + 1, end)
			return root

	def modify(self, root, index, addValue):
		if root.start <= root.end:
			if index >= root.start and index <= root.end:
				root.count += addValue
				if root.start != root.end:
					mid = (root.start + root.end) // 2
					if index <= mid:
						self.modify(root.left, index, addValue)
					else:
						self.modify(root.right, index, addValue)

	def query(self, root, start, end):
		start = max(root.start, start)
		end = min(root.end, end)
		if start > end:
			return 0
		if root.start == root.end:
			return root.count
		if root.start == start and root.end == end:
			return root.count
		mid = (root.start + root.end) // 2
		if end <= mid:
			return self.query(root.left, start, end)
		if start > mid:
			return self.query(root.right, start, end)
		return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)



nums = [1, 2, 7, 8, 5]

inst = Solution()
print(inst.countOfSmallerNumber(nums))