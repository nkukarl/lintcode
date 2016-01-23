'''
Thoughts:

Record the position of top, bottom, left and right
Use dir to record the direction that the spiral shall go
dir plus 1 and mod 4 at the end of each iteration

'''

class Solution:
	def spiralOrder(self, matrix):
		if not matrix:
			return []
		top, bottom = 0, len(matrix) - 1
		left, right = 0, len(matrix[0]) - 1
		res = []
		dir = 0
		while top <= bottom and left <= right:
			if dir == 0:
				for col in range(left, right + 1):
					res.append(matrix[top][col])
				top += 1
			elif dir == 1:
				for row in range(top, bottom + 1):
					res.append(matrix[row][right])
				right -= 1
			elif dir == 2:
				for col in range(right, left - 1, -1):
					res.append(matrix[bottom][col])
				bottom -= 1
			else:
				for row in range(bottom, top - 1, -1):
					res.append(matrix[row][left])
				left += 1
			dir = (dir + 1) % 4

		return res

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4]]
# matrix = [[1], [2], [3], [4]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

inst = Solution()
print(inst.spiralOrder(matrix))