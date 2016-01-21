class Solution:
	def recoverRotatedSortedArray(self, nums):
		if len(nums) >= 2:
			if nums[-1] > nums[0]:
				return

		for i in range(len(nums)):
			if nums[i] > nums[i + 1]:
				pivot = i
				break

		self.helper(nums, 0, pivot)
		self.helper(nums, pivot + 1, len(nums) - 1)
		self.helper(nums, 0, len(nums) - 1)

	def helper(self, nums, i, j):
		while i < j:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1

# nums = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
nums = [1, 2, 3, 4]
# nums = [2, 3, 4, 1]
# nums = [3, 4, 1, 2]
# nums = [4, 1, 2, 3]
inst = Solution()
inst.recoverRotatedSortedArray(nums)
print(nums)
