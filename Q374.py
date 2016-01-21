class Solution:
	def spiralOrder(self, matrix):
		if not matrix:
			return []
		top, bottom = 0, len(matrix) - 1
		left, right = 0, len(matrix[0]) - 1
		res = []
		direction = 0
		while top <= bottom and left <= right:
			if direction == 0:
				for col in range(left, right + 1):
					res.append(matrix[top][col])
				top += 1
			elif direction == 1:
				for row in range(top, bottom + 1):
					res.append(matrix[row][right])
				right -= 1
			elif direction == 2:
				for col in range(right, left - 1, -1):
					res.append(matrix[bottom][col])
				bottom -= 1
			else:
				for row in range(bottom, top - 1, -1):
					res.append(matrix[row][left])
				left += 1
			direction = (direction + 1) % 4

		return res

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4]]
# matrix = [[1], [2], [3], [4]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

inst = Solution()
print(inst.spiralOrder(matrix))