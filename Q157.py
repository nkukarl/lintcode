class Solution:
	def isUnique(self, string):
		return len(string) == len(set(list(string)))

	def isUnique_1Space(self, string):
		for i in range(len(string)):
			for j in range(i + 1, len(string)):
				if string[i] == string[j]:
					return False
		return True