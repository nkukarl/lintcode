class Solution:
	def uniquePathsWithObstacles(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [[0] * n for _ in range(m)]
		if grid[0][0] == 1:
			return 0
		else:
			dp[0][0] = 1
		for col in range(1, n):
			if grid[0][col] == 0:
				dp[0][col] = 1
			else:
				break

		for row in range(1, m):
			if grid[row][0] == 0:
				dp[row][0] = 1
			else:
				break
		for row in range(1, m):
			for col in range(1, n):
				if grid[row][col] == 0:
					dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
				else:
					dp[row][col] = 0
		return dp[-1][-1]

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid = [[1]]
# grid = [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0]]

inst = Solution()
print(inst.uniquePathsWithObstacles(grid))