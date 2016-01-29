'''
Thoughts:

Define Pair class with index and SUM attributes
SUM is used to store the sum of numbers up to position index in array nums (exclusive)

Initialise summary with [Pair[0, 0]]
Iterate all the numbers in nums and update summary, since SUM is used to store the sum of numbers up to position index in array nums (exclusive), save i + 1 as index instead of i
Sort summary using its SUM attribute
Iterate all the pairs in summary, find out the smallest absolute value of difference between adjacent pairs
Update closest and store the indices
Be aware that since Pair stores exclusive index, 1 shall be subtracted from index before being added to tmp
However, for the lower bound, 1 shall be added back
If closest is equal to 0 (the minimum achievable), direct return indices and exit the iteration
Otherwise, return indices outside the iteration


'''

class Pair:
	def __init__(self, index, SUM):
		self.index, self.SUM = index, SUM

class Solution:
	def subarraySumClosest(self, nums):
		if not nums:
			return []

		summary = [Pair(0, 0)]

		for i in range(len(nums)):
			summary.append(Pair(i + 1, summary[-1].SUM + nums[i]))

		summary.sort(key = lambda x: x.SUM)

		closest = 2 ** 31

		indices = [None, None]

		for i in range(1, len(summary)):
			diff = abs(summary[i].SUM - summary[i - 1].SUM)
			if diff < closest:
				closest = diff
				tmp = [summary[i].index - 1, summary[i - 1].index - 1]
				indices = [min(tmp) + 1, max(tmp)]
				if closest == 0:
					return indices

		return indices

nums = [-3, 1, 1, -3, 5]

inst = Solution()
print(inst.subarraySumClosest(nums))