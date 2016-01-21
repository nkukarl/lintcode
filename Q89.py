class Solution:
	def kSum(self, A, k, target):
		if not A:
			return 0
		A.sort()
		self.res = 0
		self.target = target
		self.k = k
		self.helper(A, [])

		return self.res

	def helper(self, A, cur):
		if len(cur) == self.k:
			if sum(cur) == self.target:
				print(cur)
				self.res += 1
		else:
			for i in range(len(A)):
				self.helper(A[i + 1:], cur + [A[i]])

A = [1, 2, 3, 4]
k = 2
target = 5

inst = Solution()
print(inst.kSum(A, k, target))
