class Solution:
	def nextPermutation(self, nums):
		if nums == sorted(nums)[::-1]:
			return nums[::-1]

		for i in range(len(nums) - 1, 0, -1):
			if nums[i - 1] < nums[i]:
				pivot = i - 1
				break

		localMin = nums[i]
		localMinPos = i
		for j in range(i, len(nums)):
			if nums[j] <= localMin and nums[j] > nums[pivot]:
				localMin = nums[j]
				localMinPos = j
		nums[pivot], nums[localMinPos] = nums[localMinPos], nums[pivot]
		tmp = nums[pivot + 1:]
		return nums[:pivot + 1] + tmp[::-1]


nums = [1, 3, 2, 3]
nums = [4, 3, 2, 1]
nums = [1, 2, 1]
# nums = [1, 3, 5, 1, 1, 2, 3, 3]
# nums = [1, 3, 8, 2, 3, 4, 5]

inst = Solution()
print(inst.nextPermutation(nums))