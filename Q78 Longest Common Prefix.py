'''
Thoughts:

Let res be initialised to ''
If strs is empty, return ''
Iterate each character of the first string in strs, let tmp = str[0][i]
Iterate all the strings in strs
If i exceed the length of strs[k], return res
Else if str[k][i] != tmp, return res
Otherwise, append tmp to res at the end of the inner iteration
Return res eventually

'''

class Solution:
	def longestCommonPrefix(self, strs):
		res = ''
		if not strs:
			return res
		for i in range(len(strs[0])):
			tmp = strs[0][i]
			for k in range(1, len(strs)):
				try:
					char = strs[k][i]
				except:
					return res
				if char != tmp:
					return res
			res += tmp
		return res

strs = ['ABCD', 'ABEF', 'ACEF']

inst = Solution()f1e
print(inst.longestCommonPrefix(strs))