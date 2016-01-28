'''
Thought:

Iterative use helper() to swap the elements of root with the smaller of the left and right child, if needed
For helper(), if the index is greater than or equal to the size of A, return
If 2 * i + 1 or 2 * i + 2 is greater than or equal to the size of A, set left and right to the maximum integer
If left < right and left < A[i], swap A[i] with left
==> A[i], A[2 * i + 1] = A[2 * i + 1], A[i]
Further helper() for 2 * i + 1
If right < A[i], swap A[i] with right
(If left < right, this belongs to condition 1, if left >= right, right is the smaller one of the left and right child)
==> A[i], A[2 * i + 2] = A[2 * i + 2], A[i]
Further helper() for 2 * i + 2

'''

class Solution:
	def heapify(self, A):
		n = len(A)
		for i in range(n // 2 - 1, -1, -1):
			self.helper(A, i)

	def helper(self, A, i):
		n = len(A)
		if i >= n:
			return

		if 2 * i + 1 >= n:
			left = 2 ** 31
		else:
			left = A[2 * i + 1]

		if 2 * i + 2 >= n:
			right = 2 ** 31
		else:
			right = A[2 * i + 2]

		if left < right and left < A[i]:
			A[i], A[2 * i + 1] = A[2 * i + 1], A[i]
			self.helper(A, 2 * i + 1)
		elif right < A[i]:
			A[i], A[2 * i + 2] = A[2 * i + 2], A[i]
			self.helper(A, 2 * i + 2)