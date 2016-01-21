class Solution:
	def isPalindrome(self, s):
		s = s.lower()
		tmp = ''
		for char in s:
			if char.isalnum():
				tmp += char
		return tmp == tmp[::-1]