'''
Thoughts:

Loop solution is trivial

Sort nums and each query do a binary search to find out the insertion position

Build segment tree using node with three attributes, start, end and count
Start and end ranges from 0 to 10000, count is initialised with 0 for each node
Iterate all the integers in nums, update the count for each node
For each query, do a query in the segment tree

'''

class Solution_binarySearch:
	def countOfSmallerNumber(self, nums, queries):
		nums.sort()
		res = []
		for q in queries:
			res.append(self.binarySearch(nums, q))
		return res

	def binarySearch(self, nums, n):
		if not nums:
			return 0
		if n <= nums[0]:
			return 0
		if n > nums[-1]:
			return len(nums)
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < n:
				head = mid + 1
			else:
				tail = mid
		return head

class Solution_loop:
	def countOfSmallerNumber(self, nums, queries):
		res = []
		for q in queries:
			counter = 0
			for n in nums:
				if n < q:
					counter += 1
			res.append(counter)
		return res

class segmentTreeNode:
	def __init__(self, start, end, max):
		self.start, self.end, self.max = start, end, max
		self.left, self.right = None, None

class Solution_segmentTree:
	def countOfSmallerNumber(self, nums, queries):
		if not nums:
			return [0] * len(queries)
		root = self.build(nums, 0, len(nums) - 1)
		res = []
		for q in queries:
			res.append(self.helper(root, q))
		return res

	def helper(self, root, n):
		if n > root.max:
			return root.end - root.start + 1
		if root.start == root.end:
			return 0
		return self.helper(root.left, n) + self.helper(root.right, n)


	def build(self, nums, start, end):
		if start <= end:
			root = segmentTreeNode(start, end, max(nums[start : end + 1]))
			if start != end:
				mid = (start + end) // 2
				root.left = self.build(nums, start, mid)
				root.right = self.build(nums, mid + 1, end)
			return root

class segmentTreeNode_opt:
	def __init__(self, start, end, count):
		self.start, self.end, self.count = start, end, count
		self.left, self.right = None, None

class Solution_segmentTree_opt:
	def countOfSmallerNumber(self, nums, queries):
		root = self.build(0, 10000)
		for n in nums:
			self.modify(root, n, 1)

		res = []
		for q in queries:
			if q <= 0:
				res.append(0)
			else:
				res.append(self.query(root, 0, q - 1))
		return res


	def build(self, start, end):
		if start <= end:
			root = segmentTreeNode_opt(start, end, 0)
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



nums, queries = [1, 2, 7, 8, 5], [1, 8, 5, 100, 0, 3]

inst = Solution_segmentTree_opt()
print(inst.countOfSmallerNumber(nums, queries))