'''
Thought:

DFS
Remember to sort nums and use set to remove duplicates

'''
class Solution:
	def permuteUnique(self, nums):
		if not nums:
			return []
		nums.sort()
		self.res = set()
		self.helper(nums, ())
		return [list(r) for r in self.res]

	def helper(self, nums, cur):
		if not nums:
			self.res.add(cur)
		else:
			for i in range(len(nums)):
				self.helper(nums[:i] + nums[i + 1:], cur + (nums[i], ))

nums = [1, 2, 2, 4]

inst = Solution()
print(inst.permuteUnique(nums))
