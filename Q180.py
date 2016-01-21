class Solution:
	def binaryRepresentation(self, n):
		if n == '0':
			return 0
		if n[0] == '-':
			n = n[1:]
			sign = '-'
		else:
			sign = ''
		integer, decimal = n.split('.')
		decimal = float('0.' + decimal)
		integer = int(integer)

		DEC = self.decimalProcessing(decimal)
		if DEC == 'ERROR':
			return DEC
		INT = bin(integer)[2:]
		res = sign + INT + '.' + DEC
		return res

	def decimalProcessing(self, decimal):
		val = 0.5
		res = ''
		counter = 0
		while counter < 32 and decimal:
			if decimal >= val:
				res += '1'
				decimal -= val
			else:
				res += '0'
			val /= 2
			counter += 1
		if decimal:
			return 'ERROR'
		return res




n = '-3.5'
# n = '3.5'

inst = Solution()
print(inst.binaryRepresentation(n))
# print(inst.decimalProcessing(0.875))