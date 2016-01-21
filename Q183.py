class Solution:
	def woodCut(self, L, k):
		if sum(L) < k:
			return 0
		minL, maxL = 0, max(L)
		while minL < maxL:
			midL = (minL + maxL) // 2
			counter = 0
			for l in L:
				counter += l // midL
			if counter >= k:
				res = midL
				minL = midL + 1
			else:
				maxL = midL
		return res

L = [232, 124, 456]
k = 1000

inst = Solution()
print(inst.woodCut(L, k))