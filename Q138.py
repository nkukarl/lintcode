class Solution:
	def subarraySum(self, nums):
		for i in range(len(nums)):
			tmp = nums[i]
			for j in range(i + 1, len(nums) + 1):
				if tmp == 0:
					return [i, j - 1]
				if j != len(nums):
					tmp += nums[j]

nums = [-3, 1, 2, -3, 4]
nums = [1, -1]

inst = Solution()
print(inst.subarraySum(nums))