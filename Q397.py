class Solution:
	def longestIncreasingContinuousSubsequence(self, A):
		if not A:
			return 0
		max1 = self.helper(A)
		A.reverse()
		max2 = self.helper(A)
		return max(max1, max2)

	def helper(self, A):
		tmp = A[0]
		maxLen = 1
		curLen = 1
		for n in A[1:]:
			if n > tmp:
				curLen += 1
			else:
				maxLen = max(maxLen, curLen)
				curLen = 1
			tmp = n
		maxLen = max(maxLen, curLen)
		return maxLen

A = [5, 1, 2, 3, 4]
A = [5, 4, 2, 1, 3]

inst = Solution()
print(inst.longestIncreasingContinuousSubsequence(A))