class Solution:
	def generateMatrix(self, n):
		nums = [i for i in range(1, n ** 2 + 1)]
		nums.reverse()
		matrix = [[0] * n for _ in range(n)]

		top, bottom = 0, n - 1
		left, right = 0, n - 1
		direction = 0
		
		while top <= bottom or left <= right:
			if direction == 0:
				for col in range(left, right + 1):
					matrix[top][col] = nums.pop()
				top += 1
			elif direction == 1:
				for row in range(top, bottom + 1):
					matrix[row][right] = nums.pop()
				right -= 1
			elif direction == 2:
				for col in range(right, left - 1, -1):
					matrix[bottom][col] = nums.pop()
				bottom -= 1
			else:
				for row in range(bottom, top - 1, -1):
					matrix[row][left] = nums.pop()
				left += 1
			direction = (direction + 1) % 4

		return matrix

inst = Solution()
print(inst.generateMatrix(3))
