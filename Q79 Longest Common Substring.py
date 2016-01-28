'''
Thought:

Dynamic programming

Initialise dp with n + 1 columns and m + 1 rows, maxLen to 0
Let dp[i][j] represent the longest common substring of A[:i + 1] and B[:j + 1]
Transfer function:
If A[i - 1] == B[j - 1], dp[i][j] = dp[i - 1][j - 1] + 1, update maxLen
Otherwise, dp[i][j] = 0

return maxLen


'''

class Solution:
	def longestCommonSubstring(self, A, B):
		m, n = len(A), len(B)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		maxLen = 0
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if A[i - 1] == B[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
					maxLen = max(dp[i][j], maxLen)
				else:
					dp[i][j] = 0
		
		return maxLen

# A, B = 'ABCD', 'BCD'

A, B = "e.com code", "r.com code"

inst = Solution()
print(inst.longestCommonSubstring(A, B))