class Solution:
	def findFirstBadVersion(self, n):
		head, tail = 1, n
		while head < tail:
			mid = (head + tail) // 2
			if SVNRepo.isBadVersion(mid):
				tail = mid
			else:
				head = mid + 1
		return head