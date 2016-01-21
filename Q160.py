class Solution:
	def findMin(self, nums):
		if not nums:
			return 0
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < nums[tail]:
				tail = mid
			elif nums[mid] > nums[tail]:
				head = mid + 1
			else:
				return min(self.findMin(nums[head : mid + 1]), self.findMin(nums[mid + 1 : tail + 1]))
		return nums[head]

nums = [4, 4, 5, 6, 7, -2, -1, -1, 0, 0, 1, 2, 3]
# nums = [9, 9, 10, 10, 11, 0, 9, 9, 9]
# nums = [1, 1, -1, 1]

inst = Solution()
print(inst.findMin(nums))