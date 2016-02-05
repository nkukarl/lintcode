'''
Thoughts:

Since each number in the array is not greater than 100, a dynamic array of size 101, dp, can be initialised
Iterate each item in dp and let dp[j] = abs(A[0] - j)
This is the minimum adjustment cost for change A[0] to each j (from 0 to 100, inclusive)

The iterate the items in A[1:], let tmp be initialised to [] at the beginning of each iteration
The minimum adjustment cost for changing the ith item into j then arises from the minimum adjustment cost for changing the (i - 1)th item into [j - target : j + target] (inclusive)
Since j - target might be smaller than 0 and j + target might be greater than 100, let low and up be max(0, j - target) and min(100, j + target) respectively
Find the smallest item in dp[low : up + 1] and tmp[j] shall be min(dp[low : up + 1]) + abs(A[i] - j)
Update dp to tmp at the end of each iteration

Return the minimum of dp after exiting the iteration

'''

class Solution:
	def MinAdjustmentCost(self, A, target):
		N = 101
		dp = [0] * N
		for j in range(N):
			dp[j] = abs(A[0] - j)

		for i in range(1, len(A)):
			tmp = []
			for j in range(N):
				low = max(0, j - target)
				up = min(N - 1, j + target)
				tmp.append(min(dp[low : up + 1]) + abs(A[i] - j))
			dp = tmp
		
		return min(dp)


A = [1, 4, 2, 3]
target = 1

inst = Solution()
print(inst.MinAdjustmentCost(A, target))