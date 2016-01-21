class Solution:
	def minPathSum(self, grid):
		if not grid:
			return 0
		row, col = len(grid), len(grid[0])
		dp = [[0] * col for _ in range(row)]
		dp[0][0] = grid[0][0]
		for r in range(1, row):
			dp[r][0] = dp[r - 1][0] + grid[r][0]
		for c in range(1, col):
			dp[0][c] = dp[0][c - 1] + grid[0][c]
		for r in range(1, row):
			for c in range(1, col):
				dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
		# print(dp)
		return dp[-1][-1]

grid = [[1, 1, 2], [4, 7, 1], [3, 2, 5], [3, 6, 1]]

inst = Solution()
print(inst.minPathSum(grid))