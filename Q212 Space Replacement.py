'''
Trivial
'''

class Solution:
	def replaceBlank(self, string, length):
		string = [char for char in string]
		for i in range(length):
			if string[i] == ' ':
				string[i] = '%20'
		return string