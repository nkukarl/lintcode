'''
Thoughts:

Some simple corner case to start, if the minimum of A is greater than or equal to zero, then the sum of A would give the maximum subarray sum, return [0, len(A) - 1]
If the maximum of A is smaller than or equal to zero, then the largest element would give the maximum subarray sum, return [A.index(min(A)), A.index(min(A))]
Otherwise, let cur, MAX, left and right be initialised to 0
Iterate all the numbers in A using its index
In each iteration, let cur = cur + A[i]
If cur is less than 0, change cur back to 0 and let left be i + 1 since all the numbers to the left can be ignored
Otherwise, compare cur with MAX, if cur is greater than MAX, update right to i, and update res to [left, right], update MAX to cur
Return res

'''

class Solution:
	def continuousSubarraySum(self, A):
		if min(A) >= 0:
			return [0, len(A) - 1]
		if max(A) <= 0:
			return [A.index(max(A)), A.index(max(A))]
		MAX, cur = 0, 0
		left, right = 0, 0
		res = [left, right]
		for i in range(len(A)):
			cur += A[i]
			if cur < 0:
				cur = 0
				left = i + 1
			else:
				if cur > MAX:
					MAX = cur
					right = i
					res = [left, right]

		return res

nums = [-3, 1, 3, -3, 4]
nums = [-4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -1000]

inst = Solution()
print(inst.continuousSubarraySum(nums))