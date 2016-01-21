class Solution:
	def longestIncreasingSubsequence(self, nums):
		if not nums:
			return 0
		dp = [1] + [0] * (len(nums) - 1)
		for i in range(1, len(nums)):
			for j in range(i):
				if nums[j] <= nums[i]:
					dp[i] = max(dp[i], dp[j])
			dp[i] += 1
		return max(dp)

nums = [5, 4, 1, 2, 3]
nums = [4, 2, 4, 5, 3, 7]

inst = Solution()
print(inst.longestIncreasingSubsequence(nums))