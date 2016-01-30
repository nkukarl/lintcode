'''
Thoughts:

Similar to Maximum Subarray II

The difference is that in addition to calculate the ongoing maximum subarray sum, the ongoing minimum subarray sum shall be calculated as well
And this has to be done for nums both from left to right and right to left
The four arrays are denoted as l2rMax, l2rMin, r2lMax, r2lMin

Similarly, pop the last element of l2rMax and l2rMin and pop the first element of r2lMax and r2lMin

The maximum subarray difference then arise from the absolute value of elementwise difference between l2rMax and r2lMin (denoted as tmp1), or between l2rMin and r2lMax (denoted as tmp2)

Return the maximum of tmp1 and tmp2

'''


class Solution:
	def maxDiffSubArrays(self, nums):
		l2rMax = self.maxSubarray(nums)
		l2rMin = self.minSubarray(nums)

		r2lMax = self.maxSubarray(nums[::-1])[::-1]
		r2lMin = self.minSubarray(nums[::-1])[::-1]

		l2rMax.pop()
		l2rMin.pop()

		r2lMax.pop(0)
		r2lMin.pop(0)

		tmp1 = max([abs(a - b) for a, b in zip(l2rMax, r2lMin)])
		tmp2 = max([abs(a - b) for a, b in zip(l2rMin, r2lMax)])

		return max(tmp1, tmp2)

	def maxSubarray(self, nums):
		res = [nums[0]]
		cur = max(0, nums[0])
		for n in nums[1:]:
			cur += n
			if cur < 0:
				cur = 0
				res.append(max(n, res[-1]))
			else:
				res.append(max(cur, res[-1]))

		return res

	def minSubarray(self, nums):
		res = [nums[0]]
		cur = min(0, nums[0])
		for n in nums[1:]:
			cur += n
			if cur > 0:
				cur = 0
				res.append(min(n, res[-1]))
			else:
				res.append(min(cur, res[-1]))

		return res

nums = [1, 2, -3, 1]

inst = Solution()
print(inst.maxDiffSubArrays(nums))