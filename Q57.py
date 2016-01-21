class Solution:
	def threeSum(self, nums):
		nums.sort()
		res = set()
		for i in range(len(nums) - 2):
			newTarget = -nums[i]
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
		return [list(r) for r in res]

nums = [-1, 0, 1, 2, -1, -4]

inst = Solution()
print(inst.threeSum(nums))