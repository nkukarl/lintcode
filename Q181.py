class Solution:
	def bitSwapRequired(self, a, b):
		c = a ^ b
		counter = 0
		move = 0
		while c and move < 32:
			counter += c & 1
			c >>= 1
			move += 1
		return counter

a, b = 1, -1

inst = Solution()
print(inst.bitSwapRequired(a, b))