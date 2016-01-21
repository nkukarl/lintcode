class Solution:
	def myPow(self, x, n):
		if x == 0:
			return 0
		if n == 1:
			return x
		if n == 0:
			return 1
		if n < 0:
			flag = 1
		else:
			flag = 0
		n = abs(n)
		res = 1
		while n:
			if n & 1:
				res *= x
			n >>= 1
			x = x * x
		if flag:
			return 1 / res
		return res

x, n = 2.1, 3
x, n = 0, 1
x, n = 1, 0
x, n = 34.00515, -3

inst = Solution()
print(inst.myPow(x, n))