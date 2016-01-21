class Solution:
	def trailingZeros(self, n):
		m = n
		exp = 0
		while m >= 5:
			m //= 5
			exp += 1
		if exp < 1:
			return exp
		mult = n // (5 ** exp)
		rem = n - mult * (5 ** exp)
		return mult * self.trailingZerosHelper(exp) + self.trailingZeros(rem)

	def trailingZerosHelper(self, exp):
		res = [0]
		for i in range(exp):
			res.append(res[-1] * 5 + 1)
		return res[-1]

inst = Solution()
print(inst.trailingZeros(20))

print(inst.trailingZerosHelper(4))