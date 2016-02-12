class Solution:
	def minCut(self, s):
		n = len(s)
		dp = [[0] * n for _ in range(n)]
		for i in range(n - 1, -1, -1):
			for j in range(i, n):
				if ((j - i < 2) or (dp[i + 1][j - 1])) and s[i] == s[j]:
					dp[i][j] = 1
		# print(dp)
		res = [-1] + [2 ** 31] * (n)
		for i in range(1, n + 1):
			for j in range(i - 1, -1, -1):
				if dp[j][i - 1]:
					res[i] = min(res[i], res[j] + 1)
		# print(res)
		return res[-1]

s = 'adddbbddd'

inst = Solution()
print(inst.minCut(s))