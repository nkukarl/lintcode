'''
Thoughts:

Simple binary search
'''
class Solution:
	def searchInsert(self, A, target):
		if not A:
			return 0
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


A = [1, 3, 5, 6]
target = 0

inst = Solution()
print(inst.searchInsert(A, target))