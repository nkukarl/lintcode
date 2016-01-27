'''
Thoughts:

Initialise summary with [0] * 32
Iterate all the numbers in A, for each n, check all of its bits and update summary array
Mod every elements of summary array by 3
Let val = 1 and ans = 0
Iterate all the elements in summary array, add current val to ans if the element is 1, double val at the end of each iteration

'''

class Solution:
	def singleNumberII(self, A):
		summary = [0] * 32
		for n in A:
			i = 0
			while n and i < 32:
				summary[i] += n & 1
				n >>= 1
				i += 1
		# print(summary)
		val = 1
		ans = 0
		for i in range(32):
			summary[i] %= 3
			if summary[i]:
				ans += val
			val <<= 1
		return ans

A = [1, 1, 2, 3, 3, 3, 2, 2, 4, 1]

inst = Solution()
print(inst.singleNumberII(A))