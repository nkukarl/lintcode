'''
Thoughts:

Swap elements of nums aiming for num[i] == i
Second pass to find the first element with num[i] != i
If reaches the end, return n

Mathematical method is trivial:
Find the difference between sum(nums) and the sum from 1 to n (inclusive)

'''

class Solution:
	def findMissing(self, nums):
		n = len(nums)
		
		for i in range(len(nums)):
			while nums[i] >= 0 and nums[i] <= n - 1 and nums[nums[i]] != nums[i]:
				nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
		
		for i in range(len(nums)):
			if nums[i] != i:
				return i
		return n
		
	def findMissing_math(self, nums):
		n = len(nums)
		return n * (n + 1) // 2 - sum(nums)



nums = [0, 1, 3, 4, 6, 7, 5]

inst = Solution()
print(inst.findMissing(nums))