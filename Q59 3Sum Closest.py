'''
Thoughts:

Use closestVal and diff the denote the closest value and the minimum difference
Initialise closestVal to the sum of nums[:3] and initialise diff to abs(closestVal - target)

Iterate i in the range of 0 to len(nums) - 3 (inclusive), for each iteration of i, let j and k be initialised to i + 1 and len(nums) - 1
While j < k, let tmp = nums[i] + nums[j] + nums[k]
If tmp == target, return target (the closest is target itself)
Otherwise, if abs(tmp - target) < diff, update closestVal and diff to tmp and abs(tmp - target)
If tmp is greater than target, decrease k and if tmp is smaller than target, increase j
Return closestVal eventually


'''

class Solution:
	def threeSumClosest(self, nums, target):
		nums.sort()
		closestVal = sum(nums[:3])
		diff = abs(closestVal - target)
		for i in range(len(nums) - 2):
			j, k = i + 1, len(nums) - 1
			while j < k:
				tmp = nums[i] + nums[j] + nums[k]
				if tmp == target:
					return target
				if abs(tmp - target) < diff:
					diff = abs(tmp - target)
					closestVal = tmp
				if tmp < target:
					j += 1
				else:
					k -= 1

		return closestVal

nums = [-1, 2, 1, -4]
target = 1

inst = Solution()
print(inst.threeSumClosest(nums, target))