class Solution:
	def binarySearch(self, nums, target):
		if not nums:
			return -1
		if target not in nums:
			return -1
		head = 0
		tail = len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < target:
				head = mid + 1
			else:
				tail = mid
		return head

nums = [1, 2, 3, 3, 4, 5, 10]
target = 12

inst = Solution()
print(inst.binarySearch(nums, target))