class Solution:
	def backPack(self, m, A):
		n = len(A)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(n + 1):
			dp[i][0] = 1

		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if j < A[i - 1]:
					dp[i][j] = dp[i - 1][j]
				else:
					dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]

		tmp = dp[-1]
		while tmp:
			if tmp[-1] != 1:
				tmp.pop()
			else:
				return len(tmp) - 1

m = 11
A = [2, 3, 5, 7]

inst = Solution()
print(inst.backPack(m, A))