'''
Thoughts:

isPalindrome() is trivial:
Convert s to lower case, iterate the characters of s and only add alphanumerics to tmp
Check whether tmp is palindromic

isPalindrome_opt() uses no extra memory:
Use two pointers, left and right
If both s[left] and s[right] are alphanumerics, return False if they are not equal
If s[left]/s[right] is not an alphanumeric, add/minus left/right by 1 until they are both alphanumerics
Return True outside the iteration


'''

class Solution:
	def isPalindrome(self, s):
		s = s.lower()
		tmp = ''
		for char in s:
			if char.isalnum():
				tmp += char
		return tmp == tmp[::-1]

	def isPalindrome_opt(self, s):
		if not s:
			return True
		left, right = 0, len(s) - 1
		while left < right:
			if s[left].isalnum() and s[right].isalnum():
				if s[left].lower() != s[right].lower():
					return False
				left += 1
				right -= 1
			elif s[left].isalnum():
				right -= 1
			else:
				left += 1
		return True