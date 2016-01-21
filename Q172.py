class Solution:
	def removeElement(self, A, elem):
		if not A:
			return 0
		if elem not in A:
			return len(A)
		i, j = 0, len(A) - 1
		while i < j:
			while i < len(A) - 1 and A[i] != elem:
				i += 1
			while j > 0 and A[j] == elem:
				j -= 1
			if i < j:
				A[i], A[j] = A[j], A[i]
				i += 1
				j -= 1
		res = 0
		for a in A:
			if a != elem:
				res += 1
			else:
				break
		return res

A, elem = [0, 4, 4, 0, 4, 4, 4, 0, 2], 4

inst = Solution()
print(inst.removeElement(A, elem))
print(A)
