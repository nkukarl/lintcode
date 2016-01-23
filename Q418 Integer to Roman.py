'''
Thoughts:

Divide val by each number in nums and update val to the corresponding modulo
If division returns 1, add the corresponding roman letter(s)

'''

Int2Roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100:'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

class Solution:
	def intToRoman(self, val):
		res = ''
		for n in nums:
			quo = val // n
			res += quo * Int2Roman[n]
			val = val % n

		return res

inst = Solution()

vals = [4, 12, 21, 99]
for val in vals:
	print(inst.intToRoman(val))