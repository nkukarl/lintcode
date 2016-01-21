class Solution:
	def DeleteDigits(self, A, k):
		A = [int(a) for a in list(A)]
		toSelect = len(A) - k
		return int(self.helper(A, toSelect, ''))

	def helper(self, A, toSelect, cur):
		if toSelect == 1:
			return cur + str(min(A))
		else:
			B = A[:-(toSelect - 1)]
			num = min(B)
			C = A[B.index(num) + 1:]
			return self.helper(C, toSelect - 1, cur + str(min(B)))

A, k = '178542', 2

inst = Solution()
print(inst.DeleteDigits(A, k))