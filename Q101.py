class Solution:
	def removeDuplicates(self, A):
		if not A:
			return 0
		cur = A[0]
		counter = 1
		i, j = 0, 1
		while j < len(A):
			if A[j] != cur:
				i += 1
				cur = A[j]
				counter = 1
				A[i], A[j] = A[j], A[i]
			else:
				if counter == 1:
					i += 1
					counter += 1
					A[i], A[j] = A[j], A[i]
			j += 1
		return i + 1

A = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 7]
A = [-14,-14,-14,-14,-14,-14,-14,-13,-13,-13,-13,-12,-11,-11,-11,-9,-9,-9,-7,-7,-7,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-2,-1,-1,0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,7,7,7,7,8,8,8,8,9,9,10,10,11,11,11,11,11,12,12,12,12,13,13,13,13,14,14,15,16,17,18,18,18,20,20,21,21,21,21,21,22,22,22,22,23,24,24,25]
inst = Solution()
print(inst.removeDuplicates(A))
print(A)