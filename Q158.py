class Solution:
	def anagram(self, s, t):
		stat1 = self.stringStat(s)
		stat2 = self.stringStat(t)
		return stat1 == stat2

	def stringStat(self, s):
		res = dict()
		for char in s:
			res[char] = res.get(char, 0) + 1
		return res

s, t = 'abcd','dcab'

inst = Solution()
print(inst.anagram(s, t))		