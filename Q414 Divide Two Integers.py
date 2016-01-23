'''
Thoughts:

Bit manipulation

Record the sign
Convert dividend and divisor to abs
Left shift 1 and divisor until divisor > dividend
The number of right shifts determines how many time 1 is doubled
Keep right shifting divisor and compare dividend and divisor,
If dividend >= divisor, add the value to corresponding right shifted "1" to result, dividend -= divisor
Right shift "1" and divisor

Multiply res by the sign and be careful with overflow issue

'''

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
