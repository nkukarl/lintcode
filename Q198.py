class Solution:
	def permutationIndexII(self, A):
		copyA = sorted(A[::])
		counter = 0
		for n in A:
			tmp = copyA[:copyA.index(n)]
			tmp = list(set(tmp))
			for t in tmp:
				copyAA = copyA[::]
				copyAA.remove(t)
				counter += self.perm(copyAA)
			copyA.remove(n)
		return counter + 1

	def perm(self, A):
		summary = dict()
		for n in A:
			summary[n] = summary.get(n, 0) + 1
		res = self.factorial(len(A))
		for val in summary.values():
			res //= self.factorial(val)
		return res

	def factorial(self, n):
		if n <= 1:
			return 1
		res = 1
		i = 2
		while i <= n:
			res *= i
			i += 1
		return res

A = [4, 2, 1, 2]

inst = Solution()
print(inst.permutationIndexII(A))