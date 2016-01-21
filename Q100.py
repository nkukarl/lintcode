class Solution:
	def removeDuplicates(self, A):
		i, j = 0, 1
		while j < len(A):
			if A[j] != A[i]:
				i += 1
				A[i], A[j] = A[j], A[i]
			j += 1
		return i + 1

A = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6]
inst = Solution()
print(inst.removeDuplicates(A))
print(A)