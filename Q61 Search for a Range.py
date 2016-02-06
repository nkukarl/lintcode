'''
Thoughts:

Advanced binary search

If A is empty, or target is smaller than the minimum of A or target is greater than the maximum of A, return [-1, -1]
Binary search target, check whether A has target at the start position
If not, return [-1, -1]
Otherwise, binary search target + 1, the end position shall be the start position of the next number minus 1

Return [start, end]

'''
class Solution:
	def searchRange(self, A, target):
		if not A or target > A[-1] or target < A[0]:
			return [-1, -1]
		start = self.binarySearch(A, target)
		if A[start] != target:
			return [-1, -1]
		end = self.binarySearch(A, target + 1) - 1
		return [start, end]

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