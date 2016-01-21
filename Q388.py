factorials = [1, 1]
for n in range(2, 9):
	factorials.append(factorials[-1] * n)

class Solution:
	def getPermutation(self, n, k):
		m = n - 1
		k -= 1
		quo = []
		while m:
			quo.append(k // factorials[m])
			k = k % factorials[m]
			m -= 1
		quo.append(0)
		print(quo)
		candidates = [i for i in range(1, n + 1)]
		res = ''
		for q in quo:
			res += str(candidates.pop(q))
		return res

n, k = 6, 539
n, k = 3, 1

inst = Solution()
print(inst.getPermutation(n, k))