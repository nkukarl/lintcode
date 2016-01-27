'''
Thoughts:

Split n into integer and decimal
Check whether n is negative or positive and initialise sign to '-' or ''
Remove the first char of integer if needed
Convert integer into binary using bin()
If decimal is '' or decimal == '0', the original number is an integer
Return sign + integer

Convert decimal from string to float after inserting '0.' before decimal
Initialise tmp to '', val to 0.5 and counter to 0
While decimal is not 0 and counter is less than 32,
Check if decimal is larger than or equal to current val
Append '1' to tmp if it is True, subtract current val from decimal
Otherwise append '0'
Update val to half of its original value and add 1 to counter for each loop
If the loop exists with decimal equal to 0, the original number can be represented by no more than 32 bits, return sign + integer + '.' + tmp
Otherwise, the maximum number of bits has been reached before decimal becomes zero, return ERROR

'''

class Solution:
	def binaryRepresentation(self, n):
		integer, decimal = n.split('.')
		if integer[0] == '-':
			sign = '-'
			integer = integer[1:]
		else:
			sign = ''
		integer = bin(int(integer))[2:]
		if not decimal or int(decimal) == 0:
			return sign + integer
		decimal = float('0.' + decimal)
		tmp = ''
		val = 0.5
		counter = 0
		while decimal and counter < 32:
			if decimal >= val:
				decimal -= val
				tmp += '1'
			else:
				tmp += '0'
			val *= 0.5
			counter += 1
		if decimal == 0:
			return sign + integer + '.' + tmp
		return 'ERROR'




n = '-3.5'
# n = '3.5'

inst = Solution()
print(inst.binaryRepresentation(n))
# print(inst.decimalProcessing(0.875))