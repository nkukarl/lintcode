class Solution:
	def threeSumClosest(self, nums, target):
		nums.sort()
		closest = sum(nums[:3])
		closest_diff = abs(closest - target)
		for i in range(len(nums) - 2):
			j, k = i + 1, len(nums) - 1
			while j < k:
				tmp = nums[i] + nums[j] + nums[k]
				if tmp == target:
					return target
				else:
					if abs(tmp - target) < closest_diff:
						closest_diff = abs(tmp - target)
						closest = tmp
					if tmp < target:
						j += 1
					else:
						k -= 1

		return closest

nums = [-1, 2, 1, -4]
target = 1

inst = Solution()
print(inst.threeSumClosest(nums, target))