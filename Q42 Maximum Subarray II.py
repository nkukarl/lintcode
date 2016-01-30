'''
Thoughts:

Similar to maximum array problem, the only difference is to store the current maximum in an array res and return res in helper() when iterating nums from the left, denoted as l2r
Reverse nums and reapply helper() to obtain the current maximum from right, denoted as r2l, reverse r2l as well
However, since the tow subarrays cannot overlap and there is a least one element in a subarray, the last element of l2r can be ignored since only one subarray can be formed
Similarly, the first element of r2l can also be ignored
Next, simply add the elements in l2r and r2l in elementwise manner and return the largest of the sum

'''

class Solution:
	def maxTwoSubArrays(self, nums):
		if not nums:
			return 0
		l2r = self.helper(nums)
		nums.reverse()
		r2l = self.helper(nums)
		r2l.reverse()
		tmp = [a + b for a, b in zip(l2r[:-1], r2l[1:])]
		return max(tmp)


	def helper(self, nums):
		res = [nums[0]]
		cur = max(nums[0], 0)
		for n in nums[1:]:
			cur += n
			if cur < 0:
				cur = 0
				res.append(max(n, res[-1]))
			else:
				res.append(max(cur, res[-1]))
		return res


nums = [1, 3, -1, 2, -1, 2]
# nums = [-1, -1]
nums = [-1, -2, -3, -100, -1, -50]
nums = [-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]

inst = Solution()
print(inst.maxTwoSubArrays(nums))