class Solution:
	def productExcludeItself(self, A):
		left2Right = [A[0]]
		for n in A[1:]:
			left2Right.append(left2Right[-1] * n)
		left2Right = [1] + left2Right + [1]
		A = A[::-1]
		right2Left = [A[0]]
		for n in A[1:]:
			right2Left.append(right2Left[-1] * n)
		right2Left = right2Left[::-1]
		right2Left = [1] + right2Left + [1]
		res = []
		for i in range(1, len(A) + 1):
			res.append(left2Right[i - 1] * right2Left[i + 1])
		return res

A = [1, 2, 3, 4, 5, 6]

inst = Solution()
print(inst.productExcludeItself(A))