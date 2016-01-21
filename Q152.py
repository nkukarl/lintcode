class Solution:
	def combine(self, n, k):
		nums = [i for i in range(1, n + 1)]
		self.k = k
		self.res = []
		self.helper(nums, [])
		return self.res

	def helper(self, nums, cur):
		if len(cur) == self.k:
			self.res.append(cur)
		else:
			for i in range(len(nums)):
				self.helper(nums[i + 1:], cur + [nums[i]])

n, k = 5, 2

inst = Solution()
print(inst.combine(n, k))