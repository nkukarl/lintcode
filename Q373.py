class Solution:
	def partitionArray(self, nums):
		slow = 0
		while slow < len(nums) and nums[slow] % 2 == 1:
			slow += 1
		fast = slow + 1
		while fast < len(nums):
			if nums[fast] % 2 == 1:
				nums[slow], nums[fast] = nums[fast], nums[slow]
				slow += 1
			fast += 1

import random
nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)
print(nums)

inst = Solution()
inst.partitionArray(nums)
print(nums)