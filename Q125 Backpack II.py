'''
Thoughts:

This question is a bit complicated then Q92 Backpack

backPackII_MLE() does not raise to MLE in Lintcode OJ, yet it requires m * n memory

The idea here is then to initialise dp to
[[[1, 0]] + [[0, 0]] * m for _ in range(n + 1)]
For each innermost array, the first number represents whether the corresponding size can be filled or not
If it can be filled, the second number would be the maximum corresponding value since there might be different combinations of items which give the same size but different values
If it cannot be filled, the second number would be zero (the entire innermost array would be [0, 0])

Iterate the rows and columns of dp using i and j, respectively
If j < A[i - 1], dp[i][j] would copy the value of dp[i - 1][j]
Otherwise, let val be the maximum value achievable and let val be initialised to 0
If dp[i - 1][j][0] is 1, val can be updated to the larger one of tmp and dp[i - 1][j][0]
If dp[i - 1][j - A[i - 1]] is 1, val can be update to the larger one of tmp and dp[i - 1][j - A[i - 1]] + V[i - 1]
If val != 0, update dp[i][j] to [1, val]
Otherwise, dp[i][j] is [0, 0]

The maximum size achievable, denoted as res, is included in the bottom row of dp
Let tmp equal to the bottom row, iterate tmp using iterator t and update res to the maximum value of t[1]
Return res

The optimised solution then initialise dp to an array
The iterations are the same, for each outer loop, tmp is initialised to [[1, 0]] and calculated values are appended to tmp for each inner loop
At the end of each outer loop, dp is updated to tmp

Same processing as mentioned above is then applied to dp to obtain the maximum size achievable

'''

class Solution:
	def backPackII(self, m, A, V):
		n = len(A)
		dp = [[1, 0]] + [[0, 0]] * m

		for i in range(n):
			tmp = [[1, 0]]
			for j in range(1, m + 1):
				if j < A[i]:
					if dp[j][0]:
						tmp.append(dp[j])
					else:
						tmp.append([0, 0])
				else:
					val = 0
					if dp[j][0]:
						val = max(val, dp[j][1])
					if dp[j - A[i]][0]:
						val = max(val, dp[j - A[i]][1] + V[i])
					if val:
						tmp.append([1, val])
					else:
						tmp.append([0, 0])
			dp = tmp

		res = 0
		for t in tmp:
			res = max(res, t[1])

		return res



	def backPackII_MLE(self, m, A, V):
		n = len(A)

		dp = [[[1, 0]] + [[0, 0]] * m for _ in range(n + 1)]


		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if j < A[i - 1]:
					dp[i][j] = dp[i - 1][j]
				else:
					tmp = 0
					if dp[i - 1][j][0]:
						tmp = max(tmp, dp[i - 1][j][1])
					if dp[i - 1][j - A[i - 1]][0]:
						tmp = max(tmp, dp[i - 1][j - A[i - 1]][1] + V[i - 1])

					if tmp:
						dp[i][j] = [1, tmp]

		tmp = dp[-1]
		res = 0
		for t in tmp:
			res = max(res, t[1])
		return res




m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]

inst = Solution()
print(inst.backPackII(m, A, V))