'''
Thoughts:

Binary search
Let left and right be 0 and len(A) - 1
While left < right, let mid = (left + right) // 2
If A[mid] is greater than its two neighbours, return mid
If A[mid] is greater than A[mid - 1] and smaller than A[mid + 1], the peak would exist in the right half, let left = mid + 1
Otherwise, the peak would exist in the left half, let right = mid
Return left eventually

'''
class Solution:
	def findPeak(self, A):
		left, right = 0, len(A) - 1
		while left < right:
			mid = (left + right) // 2
			if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
				return mid
			elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
				left = mid + 1
			else:
				right = mid
		return left

A = [1, 2, 1, 3, 4, 5, 7, 6]
A = [1, 2, 4, 5, 6, 7, 8, 6]

inst = Solution()
print(inst.findPeak(A))