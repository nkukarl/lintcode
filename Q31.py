class Solution:
	def partitionArray(self, nums, k):
		if not nums or k < min(nums):
			return 0
		if k > max(nums):
			return len(nums)
		fast, slow, pos = 0, 0, 0
		while nums[pos] < k:
			pos += 1
		for fast in range(pos, len(nums)):
			if nums[fast] < k:
				while nums[slow] < k:
					slow += 1
				nums[fast], nums[slow] = nums[slow], nums[fast]
		return slow + 1

import random

nums = [1, 2, 3] * 10
random.shuffle(nums)
print(nums)

# nums = [1, 3, 2, 1, 1, 2, 2, 3, 2, 1, 3, 3]
k = 2

inst = Solution()
print(inst.partitionArray(nums, k))