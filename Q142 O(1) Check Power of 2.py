'''
Thoughts:

Very elegant algorithm
If a number is power of 2, its binary form only has one 1 at the beginning
And its left adjacent number, 1 less than it, has all the bits inverted
Hence, num & num - 1 gives 0

'''

class Solution:
	def checkPowerOf2(self, n):
		if n == 0:
			return False
		return n & n - 1 == 0

inst = Solution()
for i in range(1, 21):
	print(i, inst.checkPowerOf2(i))