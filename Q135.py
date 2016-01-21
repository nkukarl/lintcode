class Solution:
	def combinationSum(self, nums, target):
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
				self.helper(nums[i:], cur + (nums[i], ))

nums = [2, 3, 6, 7]
target = 7

inst = Solution()
print(inst.combinationSum(nums, target))