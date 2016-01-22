'''
Thoughts:

Split the string using space
Reverse the split string
Iterate the split string, return the first element that is not an empty string

'''

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