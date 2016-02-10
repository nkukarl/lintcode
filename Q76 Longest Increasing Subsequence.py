class Solution:
	def longestIncreasingSubsequence(self, nums):
		if not nums:
			return 0
		n = len(nums)
		dp = [0] * n
		for i in range(n):
			for j in range(i):
				if nums[j] <= nums[i]:
					dp[i] = max(dp[i], dp[j])
			dp[i] += 1
		return max(dp)

nums = [5, 4, 1, 2, 3]
nums = [4, 2, 4, 5, 3, 7]

inst = Solution()
print(inst.longestIncreasingSubsequence(nums))