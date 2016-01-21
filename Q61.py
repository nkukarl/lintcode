class Solution:
	def searchRange(self, A, target):
		if not A or target not in A:
			return [-1, -1]
		i = self.binarySearch(A, target)
		j = self.binarySearch(A, target + 1) - 1
		return [i, j]

	def binarySearch(self, A, target):
		if target < A[0]:
			return 0
		if target > A[-1]:
			return len(A)
		head, tail = 0, len(A) - 1
		while head < tail:
			mid = (head + tail) // 2
			if A[mid] < target:
				head = mid + 1
			else:
				tail = mid
		return head

A = [5, 7, 7, 8, 8, 10]
target = 8

inst = Solution()
print(inst.searchRange(A, target))

print(inst.binarySearch(A, 6))