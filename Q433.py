class Solution:
	def numIslands(self, grid):
		if not grid:
			return 0

		counter = 0
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == 1:
					counter += 1
					self.helper(grid, row, col)

		return counter

	def helper(self, grid, row, col):
		if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == 0:
			return
		grid[row][col] = 0
		self.helper(grid, row - 1, col)
		self.helper(grid, row + 1, col)
		self.helper(grid, row, col - 1)
		self.helper(grid, row, col + 1)

grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

inst = Solution()
print(inst.numIslands(grid))