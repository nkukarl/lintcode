class Solution:
	def permutationIndex(self, nums):
		nums = nums[::-1]
		counter = 0
		tmp = [nums[0]]
		factorial = 1
		for i in range(1, len(nums)):
			tmp, k = self.binarySearchInsert(tmp, nums[i])
			factorial *= i
			counter += k * factorial

		return counter + 1

	def binarySearchInsert(self, nums, n):
		if n > nums[-1]:
			return (nums + [n], len(nums))
		if n < nums[0]:
			return ([n] + nums, 0)
		head, tail = 0, len(nums)
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < n:
				head = mid + 1
			else:
				tail = mid
		return (nums[:head] + [n] + nums[head:], head)

nums = [1, 4, 2, 2]

inst = Solution()
print(inst.permutationIndex(nums))