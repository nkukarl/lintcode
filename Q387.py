class Solution:
	def smallestDifference(self, A, B):
		B.sort()
		res = abs(A[0] - B[0])
		for n in A:
			tmp = self.binarySearch(B, n)
			print(n, tmp)
			if tmp == 0:
				return 0
			res = min(tmp, res)
		return res

	def binarySearch(self, nums, n):
		if n <= nums[0]:
			return nums[0] - n
		if n >= nums[-1]:
			return n - nums[-1]
		head, tail = 0, len(nums) - 1
		while head < tail:
			mid = (head + tail) // 2
			if nums[mid] < n:
				head = mid + 1
			else:
				tail = mid
		return min(n - nums[head - 1], nums[head] - n)

A = [6, 7, 4, 5]
B = [2, 8, 9, 3, 0]

inst = Solution()
print(inst.smallestDifference(A, B))