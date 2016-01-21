class Solution:
	def majorityNumber(self, nums):
		if not nums:
			return None
		cur = nums[0]
		count = 1
		for n in nums[1:]:
			if n == cur:
				count += 1
			else:
				count -= 1
				if count == 0:
					cur = n
					count = 1
		
		res = cur
		# check
		size = len(nums)
		count = 0
		for n in nums:
			if n == res:
				count += 1
				if count > size // 2:
					return res




nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]

inst = Solution()
print(inst.majorityNumber(nums))