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