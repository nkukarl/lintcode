class Solution:
	def previousPermutation(self, nums):
		if nums == sorted(nums):
			return nums[::-1]
		for i in range(len(nums) - 1, 0, -1):
			if nums[i - 1] > nums[i]:
				pivot = i - 1
				break
		# print(pivot, nums[pivot])
		localMax = nums[i]
		localMaxPos = i
		for j in range(i, len(nums)):
			if nums[j] >= localMax and nums[j] < nums[pivot]:
				localMax = nums[j]
				localMaxPos = j
		nums[pivot], nums[localMaxPos] = nums[localMaxPos], nums[pivot]
		# print(nums)
		tmp = nums[pivot + 1:]
		return nums[:pivot + 1] + tmp[::-1]

nums = [1, 3, 2, 3]
nums = [1, 3, 5, 1, 1, 2, 3, 3]
nums = [1, 3, 8, 2, 3, 4, 5]

inst = Solution()
print(inst.previousPermutation(nums))