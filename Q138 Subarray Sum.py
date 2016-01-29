'''
Thoughts:

Initialise summary dictionary to {0: -1} and cur to 0
Iterate all the elements in nums, and add it to cur
If cur already exists in summary, it means the sum of elements in between is zero
Hence, the left shall be summary[cur] + 1 and the right is current index: i (inclusive)

'''

class Solution:
	def subarraySum(self, nums):
		summary = {0: -1}
		cur = 0
		for i in range(len(nums)):
			cur += nums[i]
			if cur not in summary:
				summary[cur] = i
			else:
				return [summary[cur] + 1, i]


nums = [-3, 1, 2, -3, 4]
# nums = [1, -1]

inst = Solution()
print(inst.subarraySum(nums))