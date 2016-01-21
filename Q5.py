import random
class Solution:
	def kthLargestElement(self, k, A):
		pivot = random.choice(A)
		A1, A2 = [], []
		for n in A:
			if n > pivot:
				A1.append(n)
			else:
				A2.append(n)
		if len(A1) == k - 1:
			return pivot
		if len(A1) > k - 1:
			return self.kthLargestElement(k, A1)
		return self.kthLargestElement(k - len(A1), A2)
		
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