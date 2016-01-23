'''
Thoughts:

Reverse the result of lower level
Add 2 ** (current level number - 1) to the reversed results elementwise
Append temporary numbers to the result of lower level

'''

class Solution:
	def grayCode(self, n):
		res = [0]
		i = 0
		while i < n:
			tmp = res[::]
			while tmp:
				res.append(tmp.pop() + 2 ** i)
			i += 1
		return res

n = 4

inst = Solution()
print(inst.grayCode(n))

