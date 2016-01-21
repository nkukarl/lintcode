class Solution:
	"""
	@param a: The first integer
	@param b: The second integer
	@return:  The sum of a and b
	"""
	def aplusb(self, a, b):
		# write your code here, try to do it without arithmetic operators.
		MAX = 2 ** 32
		MAX_COMP = -2 ** 32
		while b:
			if b == MAX:
				return a ^ MAX_COMP
			carry = a & b
			a = a ^ b
			b = carry << 1
			print(bin(carry), bin(a), bin(b))
		return a


inst = Solution()

a = 11
b = 12
c = a + b

print(inst.aplusb(a, b), a + b)