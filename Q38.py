class Solution:
	def searchMatrix(self, matrix, target):
		if not matrix:
			return 0
		m, n = len(matrix), len(matrix[0])
		counter = 0

		# r, c = m - 1, 0
		# while r >= 0 and r <= m - 1 and c >=0 and c <= n - 1:
		# 	print(r, c, matrix[r][c])
		# 	if matrix[r][c] == target:
		# 		counter += 1
		# 		r -= 1
		# 		c += 1
		# 	elif matrix[r][c] > target:
		# 		r -= 1
		# 	else:
		# 		c += 1

		r, c = 0, n - 1
		while r >= 0 and r <= m - 1 and c >=0 and c <= n - 1:
			if matrix[r][c] == target:
				counter += 1
				r += 1
				c -= 1
			elif matrix[r][c] > target:
				c -= 1
			else:
				r += 1
		return counter

matrix = [[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]]
target = 7

inst = Solution()
print(inst.searchMatrix(matrix, target))