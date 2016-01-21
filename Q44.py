class Solution:
	def minSubArray(self, nums):
		if min(nums) >= 0:
			return min(nums)
		if max(nums) <= 0:
			return sum(nums)
		cur = 0
		minSum = 0
		for n in nums:
			cur += n
			if cur > 0:
				cur = 0
			else:
				if cur < minSum:
					minSum = cur
		return minSum

nums = [1, -1, -2, 1]

inst = Solution()
print(inst.minSubArray(nums))