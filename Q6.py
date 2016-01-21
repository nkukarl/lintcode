class Solution:
	def mergeSortedArray(self, A, B):
		a = b = 0
		if A[-1] > B[-1]:
			A, B = B, A
		C = []
		while a < len(A):
			if A[a] <= B[b]:
				C += [A[a]]
				a += 1
			else:
				C += [B[b]]
				b += 1
		C += B[b:]
		return C

A = [1, 2]
B = [2, 2]

inst = Solution()
print(inst.mergeSortedArray(A, B))