'''
Thoughts:

Initialise dp to be m rows and n columns of 0
If grid[0][0] == 1, return 0 since no path can be formed from the starting point
Assign values to the first row and first column
If current position is not an obstacle, 1 path can be formed
If there is an obstacle, break the iteration loop since no path can be formed for positions to the right and to the bottom

For other positions [i][j], if grid[i][j] == 0, dp[i][j] = dp[i - 1][j] and dp[i][j - 1] since the paths could come from both top and left
If grid[i][j] != 0, it is an obstacle, assign 0 to dp[i][j]

'''
class Solution:
	def uniquePathsWithObstacles(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [[0] * n for _ in range(m)]
		if grid[0][0] == 1:
			return 0
		dp[0][0] = 1
		for row in range(1, m):
			if grid[row][0] == 0:
				dp[row][0] = 1
			else:
				break
		for col in range(1, n):
			if grid[0][col] == 0:
				dp[0][col] = 1
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