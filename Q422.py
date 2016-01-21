class Solution:
	def lengthOfLastWord(self, s):
		s = s.split(' ')[::-1]
		for word in s:
			if word != '':
				return len(word)
		return 0

s = 'Hello World'

inst = Solution()
print(inst.lengthOfLastWord(s))