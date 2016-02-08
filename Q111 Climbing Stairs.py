'''
Thoughts:

Fibonacci

f[1] = 1, f[2] = 2
f[n] = f[n - 1] + f[n - 2] when n > 2

'''
class Solution:
	def climbStairs(self, n):
		res = [1, 1]
		if n <= 1:
			return res[n]
		a, b = 1, 1
		while n - 1:
			a, b = b, a + b
			n -= 1
		return b

inst = Solution()
for n in range(10):
	print(n, inst.climbStairs(n))
