class Solution:
	def addBinary(self, a, b):
		if len(b) > len(a):
			a, b = b, a
		a = [int(char) for char in list(a)]
		b = [int(char) for char in list(b)]
		c = []
		carry = 0
		while b:
			num1, num2 = a.pop(), b.pop()
			val = num1 ^ num2 ^ carry
			c.append(val)
			if num1 + num2 + carry >= 2:
				carry = 1
			else:
				carry = 0
		while a:
			num = a.pop()
			val = num ^ carry
			c.append(val)
			if num + carry >= 2:
				carry = 1
			else:
				carry = 0
		if carry == 1:
			c.append(carry)
		res = ''
		while c:
			res += str(c.pop())
		return res



a = '11'
b = '11'

inst = Solution()
print(inst.addBinary(a, b))