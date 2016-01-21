'''
Thoughts:

dfs problem
isPalindrome() determines whether a string is palindromic
For string s, any palindromic string starting from the beginning shall be added to "cur", the remaining string then goes into the next level recursion
When s is None, exit the recursion

'''

class Solution:
	def partition(self, s):
		self.res = []
		self.helper(s, [])
		return self.res

	def helper(self, s, cur):
		if not s:
			self.res.append(cur)
		else:
			for i in range(len(s)):
				if self.isPalindrome(s[:i + 1]):
					self.helper(s[i + 1:], cur + [s[:i + 1]])

	def isPalindrome(self, s):
		return s == s[::-1]

inst = Solution()
print(inst.partition('aabb'))