class Solution:
	def rerange(self, A):
		A.sort()
		if len(A) % 2 == 0:
			self.helper(A, 0, len(A) - 1)
		else:
			mid = A[(len(A) - 1) // 2]
			if mid > 0:
				self.helper(A, 0, len(A) - 2)
			else:
				self.helper(A, 1, len(A) - 1)
		
	def helper(self, A, i, j):
		while i < j:
			A[i], A[j] = A[j], A[i]
			i += 2
			j -= 2

A = [-1, -2, -3, -4, 5, 6, 7]
A = [-1, -2, -3, 4, 5, 6]
A = [-1, -2, -3, 4, 5, 6, 7]

inst = Solution()
inst.rerange(A)
print(A)