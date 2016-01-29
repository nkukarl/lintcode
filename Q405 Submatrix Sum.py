'''
Thoughts:

Take matrix
[
[a0, b0, c0]
[a1, b1, c1],
[a2, b2, c2]
]
as an example, iterate all the elements in each row of matrix and adding them to the values in their corresponding position in the last row of M
M changes from
[
[0, 0, 0]
]
to
[
[0, 0, 0],
[a0, b0, c0]
]
to
[
[0, 0, 0],
[a0, b0, c0],
[a0 + a1, b0 + b1, c0 + c1]
]
to
[
[0, 0, 0],
[a0, b0, c0],
[a0 + a1 + a2, b0 + b1 + b2, c0 + c1 + c2]
]

Let the top row ranges from 0 to m and the bottom row ranges from top + 1 to m + 1
Find the element-wise difference between the bottom row and the top row, this will be an array
Perform subarraySum upon the array, if None is returned, there is not subarray with a sum of 0
Otherwise, left and right will be returned
There is no need to adjust the top but the correct bottom shall be bottom - 1 since the top row of M is [0] * matrix width
Return [top, left] and [bottom, right]

If nothing can be returned by iterating the top and bottom rows, return [[-1, -1], [-1, -1]]

'''

class Solution:
	def submatrixSum(self, matrix):
		m, n = len(matrix), len(matrix[0])
		M = [[0] * n]
		for row in range(m):
			tmp = []
			for col in range(n):
				tmp.append(M[-1][col] + matrix[row][col])
			M.append(tmp)

		for top in range(m):
			for bottom in range(top + 1, m + 1):
				A = [a - b for a, b in zip(M[bottom], M[top])]
				if self.subarraySum(A):
					left, right = self.subarraySum(A)
					bottom -= 1
					return [[top, left], [bottom, right]]

		return [[-1, -1], [-1, -1]]


	def subarraySum(self, A):
		summary = {0: -1}
		cur = 0
		for i in range(len(A)):
			cur += A[i]
			if cur not in summary:
				summary[cur] = i
			else:
				return [summary[cur] + 1, i]

matrix = [[1, 5, 7], [3, 7, -8], [4, -8, 9]]

inst = Solution()
print(inst.submatrixSum(matrix))