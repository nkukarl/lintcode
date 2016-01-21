class Solution:
	def maxSquare(self, matrix):
		tmp = [0] * len(matrix[0])
		MAX = 0
		for row in range(len(matrix)):
			for col in range(len(matrix[0])):
				if matrix[row][col] == 0:
					tmp[col] = 0
				else:
					tmp[col] += 1
			MAX = max(MAX, self.maxEdge(tmp[::]))
		return MAX ** 2

	def maxEdge(self, heights):
		# print(heights)
		heights.append(0)
		MAX = 0
		stack = [-1]
		for i in range(len(heights)):
			h = heights[i]
			while h < heights[stack[-1]]:
				H = heights[stack.pop()]
				W = i - stack[-1] - 1
				MAX = max(MAX, min(H, W))
			stack.append(i)
		return MAX

matrix = [[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]

inst = Solution()
print(inst.maxSquare(matrix))


