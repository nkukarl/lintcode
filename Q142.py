class Solution:
	def checkPowerOf2(self, n):
		if n == 0:
			return False
		return n & n - 1 == 0

inst = Solution()
for i in range(1, 21):
	print(i, inst.checkPowerOf2(i))