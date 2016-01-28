'''
Thoughts:

Randomly choose a number from A as pivot
Initialise three empty arrays, A1, A2 and A3 to store the numbers greater than pivot, smaller than pivot and equal to pivot by iterating all the elements in A
If A1 contains k or more numbers, return kthLargestElement(k, A1)
Elif A1 and A3 contain less than k numbers, return kthLargestElement(k - (len(A1) + len(A3)), A2)
Otherwise, return pivot

'''

import random
class Solution:
	def kthLargestElement(self, k, A):
		pivot = random.choice(A)
		A1, A2, A3 = [], [], []
		for n in A:
			if n > pivot:
				A1.append(n)
			elif n < pivot:
				A2.append(n)
			else:
				A3.append(n)
		if len(A1) >= k:
			return self.kthLargestElement(k, A1)
		if len(A1) + len(A3) < k:
			return self.kthLargestElement(k - (len(A1) + len(A3)), A2)
		return pivot
		
	def kthLargestElement_builtin(self, k, A):
		A.sort(reverse = True)
		return A[k - 1]

inst = Solution()

# A = [5, 1, 2, 3, 4, 9, 7, 6, 8]

# for i in range(1, 10):
# 	print(inst.kthLargestElement_builtin(i, A), end = ' ')
# 	print(inst.kthLargestElement(i, A))

A = [1, 2, 3, 4, 5, 6, 8, 9, 10, 7]
random.shuffle(A)
print(A)
print(inst.kthLargestElement(4, A))
print(A)