'''
Thoughts:

A more difficult version of Find Kth Smallest Number
If the number of elements in nums is odd, k = (n + 1) // 2
Otherwise, k = n // 2

Randomly choose a number from nums, let it be the pivot
Use A1, A2 and A3 to record the numbers smaller than, greater than and equal to the pivot
If len(A1) is greater than k - 1, find the kth smallest in A1
If len(A1) + len(A3) is smaller than k, find the kth smallest in A2
Otherwise, return pivot

'''

import random

class Solution:
	def median(self, nums):
		# write your code here
		n = len(nums)
		if n % 2 == 1:
			return self.findKthSmallest(nums, (n + 1) // 2)
		return self.findKthSmallest(nums, n // 2)
		
	def findKthSmallest(self, nums, k):
		pivot = random.choice(nums)
		A1, A2, A3 = [], [], []
		for n in nums:
			if n < pivot:
				A1.append(n)
			elif n > pivot:
				A2.append(n)
			else:
				A3.append(n)
		if len(A1) > k - 1:
			return self.findKthSmallest(A1, k)
		if len(A1) + len(A3) < k:
			return self.findKthSmallest(A2, k - (len(A1) + len(A3)))
		return pivot

nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)

nums = [-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]

inst = Solution()
print(inst.median(nums))