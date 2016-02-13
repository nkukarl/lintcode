'''
Thoughts:

Initialise dp to be the m row and n columns of 1
Since for the first row and the first column, there is only one path

For position [i][j], the number of paths would be the sum of dp[i - 1][j] (coming from top) and dp[i][j - 1] (coming from left)

Return the bottom right element of dp

'''


class Solution:
	def uniquePaths(self, m, n):
		dp = [[1] * n for _ in range(m)]
		for row in range(1, m):
			for col in range(1, n):
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
		return dp[-1][-1]

inst = Solution()
print(inst.uniquePaths(3, 7))