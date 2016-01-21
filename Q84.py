class Solution:
	def singleNumberIII(self, A):
		tmp = self.singleNumber(A)

		mask = 1
		while tmp:
			if tmp & 1 == 0:
				tmp >>= 1
				mask <<= 1
			else:
				break

		A1, A2 = [], []
		for n in A:
			if n & mask == 0:
				A1.append(n)
			else:
				A2.append(n)
		print(A1, A2)

		a, b = self.singleNumber(A1), self.singleNumber(A2)

		return [a, b]

	def singleNumber(self, A):
		if not A:
			return 0
		tmp = 0
		for n in A:
			tmp ^= n
		return tmp


A = [1, 2, 2, 3, 4, 4, 9, 3]

inst = Solution()
print(inst.singleNumberIII(A))