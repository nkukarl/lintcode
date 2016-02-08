'''
Thoughts:

isInterleave_TLE() involves recursions, it could pass the test cases on Lintcode but could not pass the test cases on Leetcode

isInterleave() uses dynamic programming, let m and n be defined as the length of s1 and s2, respectively
If m + n != len(s3), there is a mismatch in the number of characters, return False
Initialise dp to [[False] * (n + 1) for _ in range(m + 1)] and let dp[0][0] = True since two empty string would form another empty string

For the first column and first row, iteratively compare s1[i - 1] and s3[i - 1]
AND s2[j - 1] and s3[j - 1]
If s1[i - 1] == s3[i - 1], dp[i][0] = True
Otherwise, break the iteration since the following in this column would be False (which is the default initialisation value)

If s2[j - 1] == s3[j - 1], dp[0][j] = True
Otherwise, break the iteration since the following in this row would be False

For row in range 1 to m (inclusive) and for column in range 1 to n(inclusive), the transfer function is
If dp[i - 1][j] and s1[i - 1] == s3[i + j - 1], dp[i][j] is True (char in s1 used to match)
If dp[i][j - 1] and s2[j - 1] == s3[i + j - 1], dp[i][j] is True (char in s2 used to match)
Otherwise, dp[i][j] is False


'''
class Solution:
	def isInterleave(self, s1, s2, s3):
		m, n = len(s1), len(s2)
		
		if m + n != len(s3):
			return False

		dp = [[False] * (n + 1) for _ in range(m + 1)]

		dp[0][0] = True
		
		for i in range(1, m + 1):
			if s1[i - 1] == s3[i - 1]:
				dp[i][0] = True
			else:
				break

		for j in range(1, n + 1):
			if s2[j - 1] == s3[j - 1]:
				dp[0][j] = True
			else:
				break

		for i in range(1, m + 1):
			for j in range(1, n + 1):
				dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])

		return dp[-1][-1]

	def isInterleave_TLE(self, s1, s2, s3):
		# print(s1, s2, s3)

		# s1, s2 and s3 all empty
		if s1 == s2 == s3 == '':
			return True
		# s3 empty, s1 not empty or s2 not empty
		if s3 == '':
			return False
		# s1 empty
		if not s1:
			return s2 == s3
		# s2 empty
		if not s2:
			return s1 == s3

		if len(s1) + len(s2) != len(s3):
			return False

		if s1[0] == s3[0] and s2[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
		if s1[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:])
		if s2[0] == s3[0]:
			return self.isInterleave(s1, s2[1:], s3[1:])

		return False

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'

s1, s2, s3 = 'aa', 'ab', 'abaa'

inst = Solution()
print(inst.isInterleave(s1, s2, s3))