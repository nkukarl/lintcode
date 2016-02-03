'''
Thoughts:

Let c equal to a ^ b, the number of 1s of c in binary format is the number of bit changes required

Right shift c until c becomes zero and the number of right shift reaches 32 since a, b and c are 32 bit integers
Let counter be initialised to 0 and adding the result of c & 1 to counter for each iteration

Return counter

'''

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