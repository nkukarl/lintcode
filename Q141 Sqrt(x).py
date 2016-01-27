'''

Newton method

a = (a + x / a) / 2
Set a precision to exit the iteration

'''

class Solution:
	def sqrt(self, x):
		if x <= 0:
			return 0
		a = x
		newA = 1
		while abs(a - newA) > 0.01:
			a = newA
			newA = (a + x / a) / 2
		return int(a)

inst = Solution()
for x in range(1, 30):
	print(x, inst.sqrt(x))