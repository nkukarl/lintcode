class Solution:
	def countAndSay(self, n):
		res = '1'
		for _ in range(n - 1):
			tmp = ''
			counter = 1
			curVal = res[0]
			for char in res[1:]:
				if char != curVal:
					tmp += str(counter) + curVal
					curVal = char
					counter = 1
				else:
					counter += 1
			res = tmp + str(counter) + curVal
		return res

inst = Solution()

for n in range(1, 7):
	print(n, inst.countAndSay(n))