class Solution:
	def solveNQueens(self, n):
		self.n = n
		self.res = []
		self.helper([], 0)
		return self.res

	def helper(self, cur, row):
		if row == self.n:
			self.res += [cur]
		else:
			for col in range(self.n):
				if self.check(cur, col):
					tmp = '.' * self.n
					self.helper(cur + [tmp[:col] + 'Q' + tmp[col + 1:]], row + 1)

	def check(self, cur, col):
		row = len(cur)
		for r in range(row):
			if cur[r][col] == 'Q':
				return False
		r, c = row, col
		while r > 0 and c > 0:
			if cur[r - 1][c - 1] == 'Q':
				return False
			r -= 1
			c -= 1

		r, c = row, col
		while r > 0 and c < self.n - 1:
			if cur[r - 1][c + 1] == 'Q':
				return False
			r -= 1
			c += 1
		return True


inst = Solution()
res = inst.solveNQueens(5)
for r in res:
	print(r)