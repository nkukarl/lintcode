class Solution:
	def kthUglyNumber(self, k):
		m3 = m5 = m7 = 0
		tmp = [1]

		for i in range(k):
			cur = min(tmp[m3] * 3, tmp[m5] * 5, tmp[m7] * 7)
			tmp += [cur]
			if cur == tmp[m3] * 3:
				m3 += 1
			if cur == tmp[m5] * 5:
				m5 += 1
			if cur == tmp[m7] * 7:
				m7 += 1
		print(tmp)
		return tmp[-1]

inst = Solution()
inst.kthUglyNumber(10)