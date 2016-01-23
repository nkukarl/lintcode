'''
Thoughts:

nums contains all the numbers that shall be filled into the matrix
Record the current top, bottom, left and right positions
Use dir to determine which direction shall the spiral go
dir plus 1 and mod 4 at the end of each iteration

'''

class Solution:
	def generateMatrix(self, n):
		nums = [i for i in range(1, n ** 2 + 1)]
		nums.reverse()
		matrix = [[0] * n for _ in range(n)]

		top, bottom = 0, n - 1
		left, right = 0, n - 1
		dir = 0
		
		while top <= bottom or left <= right:
			if dir == 0:
				for col in range(left, right + 1):
					matrix[top][col] = nums.pop()
				top += 1
			elif dir == 1:
				for row in range(top, bottom + 1):
					matrix[row][right] = nums.pop()
				right -= 1
			elif dir == 2:
				for col in range(right, left - 1, -1):
					matrix[bottom][col] = nums.pop()
				bottom -= 1
			else:
				for row in range(bottom, top - 1, -1):
					matrix[row][left] = nums.pop()
				left += 1
			dir = (dir + 1) % 4

		return matrix

inst = Solution()
print(inst.generateMatrix(3))
