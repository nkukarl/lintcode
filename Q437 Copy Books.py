class Solution:
	def copyBooks_TLE(self, pages, m):
		n = len(pages)

		pagesSum = [[0] * n for _ in range(n)]

		for i in range(n):
			for j in range(i, n):
				pagesSum[i][j] = pagesSum[i][j - 1] + pages[j]

		dp = [0] * (n + 1)
		for j in range(1, n + 1):
			dp[j] = dp[j - 1] + pages[j - 1]
		for i in range(1, m):
			tmp = []
			for j in range(n + 1):
				if j < i:
					tmp.append(dp[j])
				else:
					val = 2 ** 31
					for k in range(j):
						cur = max(dp[k], pagesSum[k][j - 1]) 
						val = min(val, cur)
					tmp.append(val)
			dp = tmp[:]
		return dp[-1]

pages, k = [2, 3, 5, 4, 2, 1], 5
# pages, k = [3, 2, 4], 2

inst = Solution()
print(inst.copyBooks(pages, k))