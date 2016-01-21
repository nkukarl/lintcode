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