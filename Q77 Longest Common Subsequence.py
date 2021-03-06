'''
Thought:

Dynamic programming

Initialise dp with n + 1 columns and m + 1 rows
Let dp[i][j] represent the longest common subsequence of A[:i + 1] and B[:j + 1]
Transfer function:
If A[i - 1] == B[j - 1], dp[i][j] = dp[i - 1][j - 1] + 1
Otherwise, dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

Return the last element of dp


'''

class Solution:
	def longestCommonSubsequence(self, A, B):
		m, n = len(A), len(B)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if A[i - 1] == B[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		return dp[-1][-1]

A = 'ABCD'
B = 'EACB'

inst = Solution()
print(inst.longestCommonSubsequence(A, B))