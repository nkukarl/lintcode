'''
Thoughts:

DFS problem

'''

class Solution:
	def subsets(self, nums):
		nums.sort()
		self.res = [[]]
		self.helper(nums, [])
		return self.res

	def helper(self, nums, cur):
		for n in nums:
			self.res.append(cur + [n])

		for i in range(len(nums)):
			self.helper(nums[i + 1:], cur + [nums[i]])

nums = [1, 2, 3, 4]

inst = Solution()
inst.subsets(nums)