class Solution:
	def divide(self, dividend, divisor):
		if divisor == 0:
			return 2 ** 31 - 1
		if dividend * divisor > 0:
			sign = 1
		else:
			sign = -1
		dividend, divisor = abs(dividend), abs(divisor)
		if dividend == divisor:
			return sign
		quo = 1
		res = 0
		while divisor <= dividend:
			quo <<= 1
			divisor <<= 1
		divisor >>= 1
		quo >>= 1
		# print(dividend, divisor, quo)
		while dividend and divisor:
			if dividend >= divisor:
				res += quo
				dividend -= divisor
			quo >>= 1
			divisor >>= 1
			# print(dividend, divisor)
		res *= sign
		if res > 2 ** 31 - 1:
			return 2 ** 31 - 1
		if res <= -2 ** 31:
			return -2 ** 31
		return res

dividend, divisor = 2 ** 31, 1

inst = Solution()
print(inst.divide(dividend, divisor))
