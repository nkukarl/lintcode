class Solution:
	def findMissing(self, nums):
		n = len(nums)
		return n * (n + 1) // 2 - sum(nums)

nums = [0, 1, 3, 4, 6, 7, 5]

inst = Solution()
print(inst.findMissing(nums))