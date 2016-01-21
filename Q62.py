class Solution:
	def search(self, nums, target):
		if target not in nums:
			return -1
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] > nums[tail]:
				head = mid + 1
			else:
				tail = mid
		pivot = head
		print('pivot:', pivot, 'nums[pivot]:', nums[pivot])
		if target <= nums[-1]:
			return pivot + self.binarySearch(nums[pivot:], target)
		else:
			return self.binarySearch(nums[:pivot], target)

	def binarySearch(self, nums, target):
		print(nums, target)
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
target = 1

inst = Solution()
print(inst.search(nums, target))