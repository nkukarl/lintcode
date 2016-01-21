class Solution:
	def longestCommonSubstring(self, A, B):
		res = 0
		m, n = len(A), len(B)
		for i in range(m):
			tmp = ''
			for j in range(n):
				a, b = A[i], B[j]
				if A[i] == B[j]:
					k1, k2 = i, j
					while k1 < m and k2 < n and A[k1] == B[k2]:
						c, d = A[k1], B[k2]
						tmp += A[k1]
						k1 += 1
						k2 += 1
					res = max(res, len(tmp))
					tmp = ''
		return res

# A, B = 'ABCD', 'BCD'

A, B = "e.com code", "r.com code"

inst = Solution()
print(inst.longestCommonSubstring(A, B))