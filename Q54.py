class Solution:
	def atoi(self, string):
		num = ''
		for char in string:
			if char.isdigit() or ((char == '-' or char == '+') and num == ''):
				num += char
			elif char == ' ' and num == '':
				continue
			else:
				break

		print(num)
		try:
			num = int(num)
			if num >= 2 ** 31:
				return 2 ** 31 - 1
			if num < -2 ** 31:
				return -2 ** 31
			return num
		except:
			return 0

string = '-1.0'
# string = '   52abc   '

string = ' +123k '

inst = Solution()
print(inst.atoi(string))