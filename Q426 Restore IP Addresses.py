'''
Thoughts:

dfs problem
Use depth as an indicator for existing recursion
When two or three digits are used as one segment, check whether segment begins with '0' or '00'
Specifically, number formed by three digits should not exceed 255
Remove duplicates using set()

'''
class Solution:
	def restoreIpAddresses(self, s):
		self.res = set()
		self.helper(s, 0, [])
		res = [r for r in self.res]
		res.sort()
		return res

	def helper(self, s, depth, cur):
		if not s:
			if depth == 4:
				self.res.add('.'.join(cur))
		else:
			self.helper(s[1:], depth + 1, cur + [s[:1]])
			if str(int(s[:2])) == s[:2]:
				self.helper(s[2:], depth + 1, cur + [s[:2]])
			if str(int(s[:3])) == s[:3] and int(s[:3]) <= 255:
				self.helper(s[3:], depth + 1, cur + [s[:3]])

s = '25525511135'
s = '1111'
s = '101023'

inst = Solution()
print(inst.restoreIpAddresses(s))