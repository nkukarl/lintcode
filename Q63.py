class Solution:
	def search(self, nums, target):
		if not nums:
			return False
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] > nums[tail]:
				head = mid + 1
			else:
				tail = mid
		pivot = head
		if target <= nums[-1]:
			pos = pivot + self.binarySearch(nums[pivot:], target)
		else:
			pos = self.binarySearch(nums[:pivot], target)
		if nums[pos] == target:
			return True
		return False

	def binarySearch(self, nums, target):
		if target < nums[0]:
			return 0
		if target > nums[-1]:
			return len(nums)
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < target:
				head = mid + 1
			else:
				tail = mid
		return head




nums = [4, 5, 1, 1, 2, 3]
target = 5

nums = [9,5,6,7,8,9,9,9,9,9,9]
target = 8

inst = Solution()
print(inst.search(nums, target))