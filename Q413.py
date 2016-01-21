class Solution:
	def reverseInteger(self, n):
		if n == 0:
			return 0
		if n < 0:
			sign = -1
		else:
			sign = 1
		n = abs(n)
		res = 0
		while n:
			val = n % 10
			n //= 10
			res = res * 10 + val
		if res > 2 ** 31:
			return 0
		return res * sign

n = 1234

inst = Solution()
print(inst.reverseInteger(n))