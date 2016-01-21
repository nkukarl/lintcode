class Solution:
	def maximumGap(self, nums):
		if len(nums) <= 1:
			return 0
		nums.sort()
		tmp1 = nums[1:]
		tmp2 = nums[:-1]
		tmp = [a - b for a, b in zip(tmp1, tmp2)]
		return max(tmp)

nums = [1, 9, 2, 5]

inst = Solution()
print(inst.maximumGap(nums))
