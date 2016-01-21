class Solution:
	def minimumTotal(self, triangle):
		if len(triangle) == 1:
			return triangle[0][0]
		left, right = self.split(triangle)
		# print(left, right)
		return triangle[0][0] + min(self.minimumTotal(left), self.minimumTotal(right))

	def split(self, triangle):
		i = 1
		left, right = [], []
		while i < len(triangle):
			left.append(triangle[i][:i])
			right.append(triangle[i][1:])
			i += 1
		return (left, right)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

inst = Solution()
print(inst.minimumTotal(triangle))

class Solution_opt:
	def minimumTotal(self, triangle):
		row = len(triangle)
		if row == 1:
			return triangle[0][0]
		dp = [triangle[0]]
		for r in range(1, row):
			tmp = [0] * (r + 1)
			for j in range(r + 1):
				if j == 0:
					tmp[j] = dp[r - 1][j] + triangle[r][j]
				elif j == r:
					tmp[j] = dp[r - 1][-1] + triangle[r][j]
				else:
					tmp[j] = min(dp[r - 1][j - 1], dp[r - 1][j]) + triangle[r][j]
			dp.append(tmp)
		return min(tmp)

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

inst = Solution_opt()
print(inst.minimumTotal(triangle))