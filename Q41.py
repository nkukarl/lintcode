class Solution:
	def maxSubArray(self, nums):
		if max(nums) <= 0:
			return max(nums)
		if min(nums) >= 0:
			return sum(nums)
		cur = 0
		maxSum = 0
		for n in nums:
			cur += n
			if cur < 0:
				cur = 0
			else:
				if cur > maxSum:
					maxSum = cur
		return maxSum

nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]

inst = Solution()
print(inst.maxSubArray(nums))