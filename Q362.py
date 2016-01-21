class Solution:
	def maxSlidingWindow(self, nums, k):
		tmp = []
		res = []
		for i in range(len(nums)):
			while tmp and nums[i] >= nums[tmp[-1]]:
				tmp.pop()
			tmp.append(i)
			if tmp[0] <= i - k:
				tmp.pop(0)
			if i >= k - 1:
				res.append(nums[tmp[0]])
		return res

nums = [1, 3, 6, 5, 2, 4, 8, 7, 9, 9, 2, 1, 6]
k = 3

inst = Solution()
print(inst.maxSlidingWindow(nums, k))