class Solution:
	def longestPalindrome(self, s):
		if s == s[::-1]:
			return s
		res = ''
		maxLen = 0
		for i in range(len(s)):
			for j in range(i + 1, len(s)):
				tmp = s[i : j + 1]
				if tmp == tmp[::-1]:
					if len(tmp) > maxLen:
						res = tmp
						maxLen = len(tmp)
		return res

class Solution_opt:
	def longestPalindrome(self, s):
		if s == s[::-1]:
			return s
		res = ''
		maxLen = 0
		for i in range(len(s)):
			for j in range(i + 1, len(s)):
				tmp = s[i : j + 1]
				if tmp == tmp[::-1]:
					if len(tmp) > maxLen:
						res = tmp
						maxLen = len(tmp)
		return res