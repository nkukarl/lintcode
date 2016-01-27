'''
Thoughts:

Initialise prevMax and prevMin using nums[0]
Let res = nums[0]
Since if nums has only one element, we shall return the first element

Iterate nums from the second element, if there is any
currMax might arise from the product of prevMax and n, prevMin and n or n itself, which also applies on currMin
Update res before assigning currMax and currMin to prevMax and prevMin for the next iteration

'''


class Solution:
	def maxProduct(self, nums):
		# currMax, currMin = nums[0], nums[0]
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
