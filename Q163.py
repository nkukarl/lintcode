class Solution:
	def numTrees(self, n):
		if n <= 1:
			return 1
		dp = [1, 1]
		while n - 1:
			tmp = 0
			for i in range(len(dp)):
				tmp += dp[i] * dp[len(dp) - i - 1]
			dp.append(tmp)
			n -= 1
		return dp[-1]

inst = Solution()
print(inst.numTrees(5))