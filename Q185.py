class Solution:
	def printZMatrix(self, matrix):
		if not matrix:
			return []
		res = []
		row, col = len(matrix), len(matrix[0])
		r, c = 0, 0
		flag = 1
		while c < col:
			flag = 1 - flag
			i = 0
			j = c
			tmp = []
			while j >= 0 and i < row:
				tmp += [matrix[i][j]]
				i += 1
				j -= 1
			if flag:
				res += tmp
			else:
				res += tmp[::-1]
			c += 1
		r = 1
		while r < row:
			flag = 1 - flag
			i = r
			j = col - 1
			tmp = []
			while j >= 0 and i < row:
				tmp += [matrix[i][j]]
				i += 1
				j -= 1
			if flag:
				res += tmp
			else:
				res += tmp[::-1]
			r += 1
		return res
		
		
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

inst = Solution()
print(inst.printZMatrix(matrix))