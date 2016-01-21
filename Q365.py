class Solution:
	def countOnes(self, num):
		counter = 0
		pos = 0
		while num and pos < 32:
			counter += num & 1
			num >>= 1
			pos += 1
		return counter

num = 1023

inst = Solution()
print(num, inst.countOnes(num))