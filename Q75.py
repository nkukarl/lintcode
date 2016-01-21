class Solution:
	def findPeak(self, A):
		head, tail = 0, len(A) - 1
		while head < tail:
			mid = (head + tail) // 2
			if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
				return mid
			elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
				head = mid + 1
			else:
				tail = mid
		return head

A = [1, 2, 1, 3, 4, 5, 7, 6]
A = [1, 2, 4, 5, 6, 7, 8, 6]

inst = Solution()
print(inst.findPeak(A))