class Solution:
	def medianII(self, nums):
		if not nums:
			return []
		tmp = [nums[0]]
		res = [nums[0]]
		for n in nums[1:]:
			tmp = self.binarySearchInsert(tmp, n)
			res += [tmp[(len(tmp) - 1) // 2]]

		return res


	def binarySearchInsert(self, nums, n):
		if n > nums[-1]:
			return nums + [n]
		if n < nums[0]:
			return [n] + nums

		head, tail = 0, len(nums)
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < n:
				head = mid + 1
			else:
				tail = mid
		return nums[:head] + [n] + nums[head:]

# nums = [4, 5, 1, 3, 2, 6, 0]
nums = [1, 2, 3, 4, 5]
nums = [2, 100, 20]

inst = Solution()
print(inst.medianII(nums))
