class Solution:
	def nextPermutation(self, nums):
		pivot = len(nums)
		for i in range(len(nums) - 1, 0, -1):
			if nums[i - 1] < nums[i]:
				pivot = i - 1
				break
		if pivot == len(nums):
			nums.reverse()
		else:
			minNum = nums[pivot + 1]
			pos = pivot + 1
			for i in range(pivot + 2, len(nums)):
				if nums[i] <= minNum and nums[i] > nums[pivot]:
					minNum = nums[i]
					pos = i
			nums[pivot], nums[pos] = nums[pos], nums[pivot]
			left, right = pivot + 1, len(nums) - 1
			while left < right:
				nums[left], nums[right] = nums[right], nums[left]
				left += 1
				right -= 1

# nums = [1, 2, 3, 4, 5, 9, 8]
nums = [1, 5, 4, 3, 2, 2, 4, 4]
nums = [5, 4, 7, 5, 3, 2]

inst = Solution()
inst.nextPermutation(nums)
print(nums)