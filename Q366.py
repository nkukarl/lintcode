class Solution:
	def fibonacci(self, n):
		n -= 1
		if n <= 1:
			return n
		a, b = 0, 1
		while n - 1:
			a, b = b, a + b
			n -= 1
		return b

inst = Solution()
for i in range(1, 10):
	print(inst.fibonacci(i))
