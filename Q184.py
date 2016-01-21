class Solution:
	def largestNumber(self, nums):
		if not nums or sum(nums) == 0:
			return '0'

		tmp = [nums[0]]

		for n in nums[1:]:
			tmp = self.binarySearchInsert(tmp, n)

		tmp = tmp[::-1]

		res = ''
		for t in tmp:
			res += str(t)
		return res


	def numCmp(self, n1, n2):
		n1, n2 = str(n1), str(n2)
		return int(n1 + n2) > int(n2 + n1)

	def binarySearchInsert(self, nums, n):
		if self.numCmp(n, nums[-1]):
			return nums + [n]
		if self.numCmp(nums[0], n):
			return [n] + nums
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if self.numCmp(n, nums[mid]):
				head = mid + 1
			else:
				tail = mid
		return nums[:head] + [n] + nums[head:]

nums = [1, 20, 23, 4, 8]
nums = [5, 13]

inst = Solution()
print(inst.largestNumber(nums))