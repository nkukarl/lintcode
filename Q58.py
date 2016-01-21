class Solution:
	def fourSum(self, nums, target):
		nums.sort()
		self.res = set()
		self.target = target
		self.helper(nums, ())
		return [list(r) for r in self.res]

	def helper(self, nums, cur):
		if len(cur) == 4:
			if sum(cur) == self.target:
				self.res.add(cur)
		else:
			for i in range(len(nums)):
				self.helper(nums[i + 1:], cur + (nums[i], ))

nums = [1, 0, -1, 0, -2, 2]

inst = Solution()
print(inst.fourSum(nums, 0))

class Solution_opt:
	def fourSum(self, nums, target):
		nums.sort()
		res = set()
		for i in range(len(nums)):
			tmp = self.threeSum(nums[i + 1:], target - nums[i])
			if tmp:
				for t in tmp:
					res.add((nums[i],) + t)
		return [list(r) for r in res]

	def threeSum(self, nums, target):
		if len(nums) < 3:
			return
		res = set()
		for i in range(len(nums) - 2):
			newTarget = target - nums[i]
			m, n = i + 1, len(nums) - 1
			while m < n:
				tmp = nums[m] + nums[n]
				if tmp == newTarget:
					res.add((nums[i], nums[m], nums[n]))
					m += 1
					n -= 1
				elif tmp < newTarget:
					m += 1
				else:
					n -= 1
		return res



nums = [1, 0, -1, 0, -2, 2]

inst = Solution_opt()
print(inst.fourSum(nums, 0))