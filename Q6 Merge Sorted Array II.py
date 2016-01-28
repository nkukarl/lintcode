'''
Thoughts:

Solution1 is trivial,
Swap A and B if the last element of A is greater than B so that the elements from A can be depleted first
Initialise an empty array, if the first element of A is smaller than or equal to the first element of B, pop the first element of A and append it to C
Otherwise, pop the first element of B and append it to C
Append B to C after the elements in A have been depleted

Solution2 uses binary search
Let the longer array (size m) be the array for inserting elements
Iterate through all the elements in the shorter array (size n) and do a binary search and insertion
Time complexity: n * log(m) where m >> n

'''

class Solution1:
	def mergeSortedArray(self, A, B):
		if A[-1] > B[-1]:
			A, B = B, A
		C = []
		while A:
			if A[0] <= B[0]:
				C += [A.pop(0)]
			else:
				C += [B.pop(0)]
		C += B
		return C

class Solution2:
	def mergeSortedArray(self, A, B):
		lA, lB = len(A), len(B)
		if lB > lA:
			A, B = B, A
		for n in B:
			A = self.binarySearchInsert(A, n)
	
		return A
		
	def binarySearchInsert(self, A, n):
		if n <= A[0]:
			return [n] + A
		if n >= A[-1]:
			return A + [n]
		
		left, right = 0, len(A) - 1
		while left < right:
			mid = (left + right) // 2
			if A[mid] < n:
				left = mid + 1
			else:
				right = mid
		
		return A[:left] + [n] + A[left:]

A = [1, 2]
B = [2, 2]

inst = Solution2()
print(inst.mergeSortedArray(A, B))