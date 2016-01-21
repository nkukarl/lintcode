class Solution:
	def mergeSortedArray(self, A, m, B, n):
		a, b = m - 1, n - 1
		for i in range(m + n - 1, -1, -1):
			if a >= 0 and b >= 0:
				if A[a] >= B[b]:
					A[i] = A[a]
					a -= 1
				else:
					A[i] = B.pop()
					b -= 1
		if B:
			for i in range(len(B)):
				A[i] = B[i]

A = [1, 6, 7, None, None]
B = [-1, 0]

inst = Solution()
inst.mergeSortedArray(A, 3, B, 2)
print(A)