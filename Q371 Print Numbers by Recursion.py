class Solution:
	def numbersByRecursion(self, n):
		return self.helper(n)[1:]

	def helper(self, n):
		if n == 0:
			return [0]
		tmp = self.helper(n - 1)
		res = []
		for i in range(10):
			for r in tmp:
				res.append(i * 10 ** (n - 1) + r)

		return res

n = 2

inst = Solution()
tmp = inst.numbersByRecursion(n)
for t in tmp:
	print(t)
