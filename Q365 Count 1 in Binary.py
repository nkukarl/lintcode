'''
Thoughts:

Right shift num and use num & 1 to determine whether the current lowest bit is 1
Be careful with negative numbers:
Since the question limit numbers to 32 bit, number of right shift should not exceed 32

'''

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