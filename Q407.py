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