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

inst = Solution()
print(inst.longestCommonPrefix(strs))