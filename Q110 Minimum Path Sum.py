'''
Thoughts:

Dynamic programming

Initialise dp to be a two-dimensional array whose size is the same as that of grid, let dp[0][0] = grid[0][0]

For the first row and first column of dp, let
dp[i][0] = dp[i - 1][0] + grid[i][0] and
dp[0][j] = dp[0][j - 1] + grid[0][j]

For i ranging from 1 to m and for j ranging from 1 to n, let
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

Return dp[-1][-1]
'''

class Solution:
    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]

grid = [[1, 1, 2], [4, 7, 1], [3, 2, 5], [3, 6, 1]]

inst = Solution()
print(inst.minPathSum(grid))