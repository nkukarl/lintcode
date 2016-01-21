class Solution:
	def firstMissingPositive(self, A):
		if 0 not in A:
			A.append(0)
		n = len(A)
		
		for i in range(n):
			while A[i] < n and A[i] >= 0 and A[i] != A[A[i]]:
				A[A[i]], A[i] = A[i], A[A[i]]
		print(A)
		for i in range(n):
			if A[i] != i:
				return i
		return n

A = [100, 4, 200, 1, 3, 2]
# A = [1]

inst = Solution()
print(inst.firstMissingPositive(A))