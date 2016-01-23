'''
Thoughts:

Reverse digits
Let carry equal to 1 at the beginning
Iterate all the digits by increasing current digit by 1 and check determine the carry for next digit, break when carry equal to 0
Outside the iteration, if carry is still 1, append 1 to the digits array
Reverse digits

'''

class Solution:
	def plusOne(self, digits):
		digits.reverse()
		carry = 1
		i = 0
		while carry and i < len(digits):
			tmp = digits[i] + carry
			digits[i] = tmp % 10
			carry = tmp // 10
			i += 1
		if carry:
			digits.append(1)
		digits.reverse()
		return digits

digits = [9, 9, 9]
digits = [1, 2, 9]
digits = []

inst = Solution()
print(inst.plusOne(digits))