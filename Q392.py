class Solution:
	def houseRobber(self, A):
		if not A:
			return 0
		if len(A) <= 2:
			return max(A)
		a, b = A[0], max(A[0], A[1])
		for n in A[2:]:
			a, b = b, max(a + n, b)
		return b

A = [3, 8, 4, 1, 5]

inst = Solution()
print(inst.houseRobber(A))