'''
Thoughts:

The basic idea is to partition an array using a value, put all the values smaller than the value given on the left and put all the values greater than the value given on the right
This is done by partition(), since compare.cmp() can only compare nuts and bolts, we will pick up one bolt from bolts and partition nuts using bolt
Return nut and pos
Here nut matches bolt and pos is the index of nut after nuts have been partitioned
nut is then used to partition bolts
nuts and bolts are then splitted into two, nuts[left : pos] and nuts[pos + 1 : right] and helper() is applied to both subarrays

'''

class Compare:
	def cmp(self, a, b):
		if a > b:
			return 1
		if a < b:
			return -1
		return 0

class Solution:
	def sortNutsAndBolts(self, nuts, bolts, compare):
		self.helper(nuts, bolts, 0, len(nuts) - 1, compare)

	def helper(self, nuts, bolts, left, right, compare):
		if left >= right:
			return
		bolt = bolts[left]
		nut, pos = self.partition(nuts, left, right, bolt, compare)
		self.partition(bolts, left, right, nut, compare)
		self.helper(nuts, bolts, left, pos - 1, compare)
		self.helper(nuts, bolts, pos + 1, right, compare)

	def partition(self, A, left, right, b, compare):
		while left < right:
			while left < right and compare.cmp(b, A[left]) == 1:
				left += 1
			while right > left and compare.cmp(A[right], b) == 1:
				right -= 1
			if left < right:
				A[left], A[right] = A[right], A[left]
			if compare.cmp(A[left], b) != 0:
				left += 1
			if compare.cmp(A[right], b) != 0:
				right -= 1
		# print(A, left, right)
		return A[left], left


import random
nuts = [1, 2, 3, 4]
bolts = [5, 3, 2, 1]
random.shuffle(nuts)
random.shuffle(bolts)
print(nuts, bolts)
compare = Compare()

inst = Solution()
inst.sortNutsAndBolts(nuts, bolts, compare)
print(nuts, bolts)