class Solution:
	def reverseWords(self, s):
		s = s.split(' ')[::-1]
		res = []
		for char in s:
			if char != '':
				res += [char]
		return ' '.join(res)

s = ' the  sky is  blue '

inst = Solution()
print(inst.reverseWord(s))