class Solution:
	def maxProduct(self, nums):
		currMax, currMin = nums[0], nums[0]
		prevMax, prevMin = nums[0], nums[0]
		res = nums[0]

		for n in nums[1:]:
			currMax = max(prevMax * n, prevMin * n, n)
			currMin = min(prevMax * n, prevMin * n, n)

			res = max(res, currMax)

			prevMax, prevMin = currMax, currMin

		return res

nums = [2, 3, -2, -3, 4]

inst = Solution()
print(inst.maxProduct(nums))
