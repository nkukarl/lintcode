'''
Thoughts:

Corner case: n < 0 and n == 0

n == 1 will be the condition for exiting the recursion

If n > 1, calculate a to the power of n // 2 mod b and assign it to res
Update res by the square of res mod b
Specifically, if n is odd, update res by multiplying res by a and then mod b


'''

class Solution:
	def fastPower(self, a, b, n):
		if n < 0:
			return -1
		if n == 0:
			return 1 % b
		if n == 1:
			return a % b
		res = self.fastPower_opt(a, b, n // 2)
		res = res ** 2 % b
		if n % 2 == 1:
			res = res * a % b
		return res

	def fastPower_wrong(self, a, b, n):
		exp = []
		while n:
			exp.append(n & 1)
			n >>= 1
		exp = exp[::-1]
		print(exp)
		rem = []
		tmp = a % b
		if tmp == 0:
			return 0
		for n in exp:
			if n:
				rem.append(tmp)
			else:
				rem.append(1)
			tmp = tmp ** 2 % b
		tmp = 1
		for r in rem:
			tmp *= r
		return tmp % b

	def check(self, a, b, n):
		return a ** n % b


a, b, n = 7898, 6, 109031
a, b, n = 109, 10000007, 1000001
# ans = 5249911

inst = Solution()
print(inst.fastPower(a, b, n))