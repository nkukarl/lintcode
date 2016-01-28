'''
Thoughts:

DFS problem
Use set to remove duplicates

'''

class Solution:
	def subsetsWithDup(self, nums):
		nums.sort()
		self.res = set()
		self.helper(nums, ())
		return [list(r) for r in self.res] + [[]]

	def helper(self, nums, cur):
		for n in nums:
			tmp = cur + (n, )
			self.res.add(tmp)

		for i in range(len(nums)):
			self.helper(nums[i + 1:], cur + (nums[i],))

nums = [1, 2, 2]

inst = Solution()
print(inst.subsetsWithDup(nums))