class Solution:
	def updateBits(self, m, n, i, j):
		if j < 31:
			mask = ~((1 << (j + 1)) - (1 << i))
		else:
			mask = (1 << i) - 1
		# print(bin(mask))
		res = (mask & m) + (n << i)
		if res > 2 ** 31:
			res -= 2 ** 32
		return res


m, n, i, j = 1024, 21, 2, 6
m, n, i, j = 1, -1, 0, 31
m, n, i, j = 456, 31, 27, 31

inst = Solution()
print(inst.updateBits(m, n, i, j))
