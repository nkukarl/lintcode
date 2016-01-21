class Solution:
	def rotate(self, matrix):
		left, right = 0, len(matrix) - 1
		top, bottom = 0, len(matrix) - 1
		while left < right:
			backup = matrix[top][left : right]
			for row in range(top, bottom):
				backup.append(matrix[row][right])
				matrix[row][right] = backup.pop(0)
			for col in range(right, left, -1):
				backup.append(matrix[bottom][col])
				matrix[bottom][col] = backup.pop(0)
			for row in range(bottom, top, -1):
				backup.append(matrix[row][left])
				matrix[row][left] = backup.pop(0)
			for col in range(left, right):
				backup.append(matrix[top][col])
				matrix[top][col] = backup.pop(0)
			left += 1
			top += 1
			right -= 1
			bottom -= 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

inst = Solution()
inst.rotate(matrix)

for line in matrix:
			print(line)
