'''
Thoughts:

A advanced version of kth smallet element

Let C = A + B

If the length of C (m) is even, return the average of the (m // 2)th and (m // 2 + 1)th smallest element of C
Otherwise, return the (m // 2)th smallest element of C

kthSmallest(C, k) randomly picks up a pivot from C, and iterates numbers in C to separate them into C1, C2 and C3
C1 has numbers smaller than pivot
C2 has numbers greater than pivot
C3 has numbers equal to pivot

If the length of C1 is greater than or equal to k, recursively run kthSmallest(C1, k)
If the sum of length of C1 and C3 is smaller than k, recursively run kthSmallest(C2, k - (len(C1) + len(C3)))
Otherwise, return pivot


'''

import random
class Solution:
	def findMedianSortedArrays(self, A, B):
		C = A + B
		m = len(C)
		if m % 2 == 1:
			return self.kthSmallest(C, m // 2 + 1)
		return (self.kthSmallest(C, m // 2) + self.kthSmallest(C, m // 2 + 1)) / 2.0

	def kthSmallest(self, C, k):
		pivot = random.choice(C)
		C1, C2, C3 = [], [], []
		for n in C:
			if n < pivot:
				C1.append(n)
			elif n > pivot:
				C2.append(n)
			else:
				C3.append(n)
		if len(C1) >= k:
			return self.kthSmallest(C1, k)
		if len(C1) + len(C3) < k:
			return self.kthSmallest(C2, k - (len(C1) + len(C3)))
		return pivot

A = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]

A = [1, 2, 3]
B = [4, 5]

inst = Solution()
print(inst.findMedianSortedArrays(A, B))