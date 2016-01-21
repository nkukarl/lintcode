class Solution:
	def wordBreak(self, s, words):
		n = len(s)
		dp = [True] + [False] * n
		for i in range(1, n + 1):
			for word in words:
				if s[i - len(word) : i] == word and dp[i - len(word)]:
					dp[i] = True
					break
		# print(dp)
		return dp[-1]

s = 'lintcodes'
# words = ['lint', 'code', 's', 'lin', 'tcode']
words = ['lint', 'codes']

inst = Solution()
print(inst.wordBreak(s, words))
