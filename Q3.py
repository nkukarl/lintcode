class Solution:
	def digitCounts(self, k, num):
		n = len(str(num))
		counter = 0
		while n > 0:
			val = 10 ** n
			quo = num // val
			rem = num % val

			counter += quo * 10 ** (n - 1)
			upperBound = (k + 1) * 10 ** (n - 1)
			lowerBound = k * 10 ** (n - 1)
			if rem >= upperBound:
				counter += 10 ** (n - 1)
			elif rem >= lowerBound:
				tmp = str(rem)[1:]
				if not tmp:
					counter += 1
				else:
					counter += int(tmp) + 1

			n -= 1

		if k == 0:
			return counter - int((len(str(num)) - 1) * '1' + '0')
		
		return counter
		

	def digitCounts_builtin(self, k, num):
		res = ''
		for i in range(num + 1):
			res += str(i)
		return res.count(str(k))

k = 5
num = 28375

inst = Solution()

for k in range(10):
	print(k, inst.digitCounts(k, num), inst.digitCounts_builtin(k, num))

