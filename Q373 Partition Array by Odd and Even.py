'''
Thoughts:

Use left and right pointer, left always searches for odd numbers and right always searches for even numbers
Swap the value at left and right until left >= right

'''

class Solution:
	def partitionArray(self, A):
		if not A:
			return
		left, right = 0, len(A) - 1
		while left < right:
			while left < right and A[left] % 2 == 1:
				left += 1
			while right > left and A[right] % 2 == 0:
				right -= 1
			A[left], A[right] = A[right], A[left]

import random
nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)
print(nums)

inst = Solution()
inst.partitionArray(nums)
print(nums)