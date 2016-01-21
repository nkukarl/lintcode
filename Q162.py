class Solution:
	def setZeroes(self, matrix):
		if not matrix:
			return
		row, col = len(matrix), len(matrix[0])
		for r in range(row):
			for c in range(col):
				if matrix[r][c] == 0:
					for j in range(col):
						if j != c and matrix[r][j] != 0:
							matrix[r][j] = 'X'
					for i in range(row):
						if i != r and matrix[i][c] != 0:
							matrix[i][c] = 'X'
					# print(matrix)
		for r in range(row):
			for c in range(col):
				if matrix[r][c] == 'X':
					matrix[r][c] = 0

# matrix = [[1, 2, 0, 3], [0, 1, 2, 3], [1, 2, 3, 4], [1, 0, 3, 2]]
matrix = [[1, 2], [0, 3]]
inst = Solution()
inst.setZeroes(matrix)
print(matrix)