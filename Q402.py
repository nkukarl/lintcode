class Solution:
	def continuousSubarraySum(self, A):
		if min(A) >= 0:
			return [0, len(A) - 1]
		if max(A) <= 0:
			return [A.index(max(A)), A.index(max(A))]
		MAX, cur = 0, 0
		tmpStart = 0
		for i in range(len(A)):
			cur += A[i]
			if cur < 0:
				cur = 0
				tmpStart = i + 1
			else:
				if cur > MAX:
					MAX = cur
					start = tmpStart
					end = i

		return [start, end]

nums = [-3, 1, 3, -3, 4]
# nums = [-4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -1000]

inst = Solution()
print(inst.continuousSubarraySum(nums))