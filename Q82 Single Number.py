'''
Thoughts:

Using a ^ a = 0, let tmp = 0, iterate items in A and let tmp = tmp ^ n
All the duplicated numbers will eventually give 0, hence tmp equals the single number

'''

class Solution:
	def singleNumber(self, A):
		if A:
			tmp = 0
			for n in A:
				tmp ^= n
			return tmp

A = [1, 2, 2, 1, 3, 4, 3]
A = []

inst = Solution()
print(inst.singleNumber(A))