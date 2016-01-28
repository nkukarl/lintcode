'''
Thoughts:

DFS problem

'''

class Solution_recursion:
	def permute(self, nums):
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

nums = [1, 2, 3]

inst = Solution_recursion()
print(inst.permute(nums))

class Solution:
	def permute(self, nums):
		if not nums:
			return []
		res = [[n] for n in nums]
		for _ in range(len(nums) - 1):
			tmp = []
			for r in res:
				numsCopy = nums[:]
				for n in r:
					numsCopy.remove(n)
				for n in numsCopy:
					tmp += [r + [n]]
			res = tmp
		return res

	def permuteUnique(self, nums):
		if not nums:
			return []
		res = set()
		for n in nums:
			res.add((n, ))
		for _ in range(len(nums) - 1):
			print(res)
			tmp = set()
			for r in res:
				numsCopy = nums[:]
				for n in r:
					numsCopy.remove(n)
				for n in numsCopy:
					tmp.add(r + (n, ))
			res = tmp
		return [list(r) for r in res]

nums = [2, 1, 2]

inst = Solution()
res = inst.permuteUnique(nums)
print(res)