'''
Thoughts:

Simple binary search
Let left and right be 1 and n respectively
If mid is a bad version, further search the first half by letting right = mid
Otherwise, let left = mid + 1
Return left

'''

class Solution:
	def findFirstBadVersion(self, n):
		left, right = 1, n
		while left < right:
			mid = (left + right) // 2
			if SVNRepo.isBadVersion(mid):
				right = mid
			else:
				left = mid + 1
		return left