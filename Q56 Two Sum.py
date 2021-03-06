'''
Thoughts:

Use a dictionary (summary) to record the numbers (dictionary key) and their indices (dictionary value)
Iterate all the items in nums, let newTarget = target - nums[i]
If newTarget exist in summary, summary[newTarget] would give the index of the first number, together with the index of current number, i, the result can be returned as [summary[newTarget] + 1, i + 1]
Otherwise, add nums[i]: i as a dictionary entry

'''

class Solution:
	def twoSum(self, nums, target):
		summary = dict()
		for i in range(len(nums)):
			newTarget = target - nums[i]
			if newTarget in summary:
				return [summary[newTarget] + 1, i + 1]
			summary[nums[i]] = i

	def twoSum_nlogn(self, nums, target):
		numsCopy = nums[:]
		nums.sort()
		i, j = 0, len(nums) - 1
		while i < j:
			tmp = nums[i] + nums[j]
			if tmp == target:
				a, b = nums[i], nums[j]
				break
			elif tmp < target:
				i += 1
			else:
				j -= 1
		print(a, b, numsCopy)
		try:
			i = numsCopy.index(a)
			j = numsCopy.index(b, i + 1)
		except:
			i = numsCopy.index(b)
			j = numsCopy.index(a, i + 1)
		return [i + 1, j + 1]


nums = [1, 0, -1]
target = -1

inst = Solution()
print(inst.twoSum(nums, target))
print(inst.twoSum_nlogn(nums, target))