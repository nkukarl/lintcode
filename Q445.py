class Solution:
	def cosineSimilarity(self, A, B):
		if len(A) != len(B):
			return 2
		n = len(A)
		numerator = 0
		denom1 = 0
		denom2 = 0
		for i in range(n):
			numerator += A[i] * B[i]
			denom1 += A[i] ** 2
			denom2 += B[i] ** 2
		denom = denom1 ** 0.5 * denom2 ** 0.5 * 1.0
		if denom == 0:
			return 2
		return numerator / denom