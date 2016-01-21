class Solution:
	def sortColors(self, nums):
		i, j = 0, len(nums) - 1
		pos = 0
		while i < j and pos < len(nums):
			while nums[i] == 0 and i < j:
				i += 1
			while nums[j] == 2 and j > i:
				j -= 1
			if i < j:
				if nums[pos] == 0 and pos > i:
					nums[pos], nums[i] = nums[i], nums[pos]
					i += 1
					pos -= 1
				elif nums[pos] == 2 and pos < j:
					nums[pos], nums[j] = nums[j], nums[pos]
					j -= 1
					pos -= 1
			pos += 1


import random

# nums = [1, 0, 1, 2, 0, 1, 0, 0, 2, 0, 1, 1]
nums = [0, 1, 2] * 4
random.shuffle(nums)
print(nums)

inst = Solution()
inst.sortColors(nums)
print(nums)

class Solution_opt:
	def sortColors(self, nums):
		pivot = len(nums)
		k = 2
		while k:
			i = 0
			for j in range(pivot):
				if nums[j] != k:
					nums[i], nums[j] = nums[j], nums[i]
					i += 1
			pivot = i
			k -= 1

nums = [0, 1, 2] * 4
random.shuffle(nums)
print(nums)

inst = Solution_opt()
inst.sortColors(nums)
print(nums)