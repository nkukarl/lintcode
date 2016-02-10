'''
Thoughts:

Sort nums in ascending order and let res be initialised to a set
Let i ranges from 0 to len(nums) - 3 (inclusive)
For each iteration of i, let j and k be initialised to i + 1 and len(nums) - 1
While j < k, let tmp be [nums[i], nums[j], nums[k]]
Compare sum(tmp) to 0
If sum(tmp) == 0, res.add((nums[i], nums[j], nums[k])), increase j and decrease k
If sum(tmp) < 0, increase j and if sum(tmp) > 0, decrease k
Return res

'''

class Solution:
	def threeSum(self, nums):
		nums.sort()
		res = set()
		for i in range(len(nums) - 2):
			j = i + 1
			k = len(nums) - 1
			while j < k:
				tmp = [nums[i], nums[j], nums[k]]
				if sum(tmp) == 0:
					res.add((nums[i], nums[j], nums[k]))
					j += 1
					k -= 1
				elif sum(tmp) < 0:
					j += 1
				else:
					k -= 1
		return [list(r) for r in res]


nums = [-1, 0, 1, 2, -1, -4]

inst = Solution()
print(inst.threeSum(nums))