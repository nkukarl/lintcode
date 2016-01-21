class Solution:
	def combinationSum2(self, nums, target):
		if not nums:
			return []
		nums.sort()
		self.target = target
		self.res = set()
		self.helper(nums, ())
		return [list(r) for r in self.res]

	def helper(self, nums, cur):
		if sum(cur) == self.target:
			self.res.add(cur)
		elif sum(cur) < self.target:
			for i in range(len(nums)):
				self.helper(nums[i + 1:], cur + (nums[i], ))

nums = [10, 1, 6, 7, 2, 1, 5]
target = 8

inst = Solution()
print(inst.combinationSum2(nums, target))