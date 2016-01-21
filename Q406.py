class Solution:
	def minimumSize(self, nums, s):
		if sum(nums) < s:
			return -1
		fast, slow = 0, 0
		minLen = len(nums)
		cur = 0
		while fast < len(nums):
			while cur < s and fast < len(nums):
				cur += nums[fast]
				fast += 1
			if cur >= s:
				while cur >= s:
					cur -= nums[slow]
					slow += 1
				minLen = min(minLen, fast - slow + 1)
		return minLen

nums, s = [2, 3, 1, 2, 4, 3], 7

inst = Solution()
print(inst.minimumSize(nums, s))