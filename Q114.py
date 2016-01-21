class Solution:
	def uniquePaths(self, m, n):
		dp = [[0] * n for _ in range(m)]
		for col in range(1, n):
			dp[0][col] = 1
		for row in range(1, m):
			dp[row][0] = 1
		for row in range(1, m):
			for col in range(1, n):
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
		return dp[-1][-1]

inst = Solution()
print(inst.uniquePaths(3, 7))