class Solution:
	def findMin(self, nums):
		if not nums:
			return 0
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < nums[tail]:
				tail = mid
			else:
				head = mid + 1
		return nums[head]

nums = [4, 5, 6, 7, -1, 0, 1, 2, 3]

inst = Solution()
print(inst.findMin(nums))