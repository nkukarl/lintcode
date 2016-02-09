'''
Thoughts:

DFS

Since the numbers in A are unique, there is no need to worry duplicated combinations of numbers

Use nums and cur to record the numbers available for use and numbers that have been selected

If the length of cur is equal to k, compare sum(cur) to target, if equal, append cur to res
Otherwise, iteratively select one element from nums and go one level deeper

'''

class Solution:
	def kSumII(self, A, k, target):
		if not A:
			return []

		self.res = []
		self.target = target
		self.k = k

		self.helper(A, [])

		return self.res

	def helper(self, nums, cur):
		if len(cur) == self.k:
			if sum(cur) == self.target:
				self.res.append(cur)
		else:
			for i in range(len(nums)):
				self.helper(nums[i + 1:], cur + [nums[i]])

A = [1, 2, 3, 4]
k = 2
target = 5

inst = Solution()
print(inst.kSumII(A, k, target))
