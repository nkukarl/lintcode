'''
Thoughts:

stringStat() summarises the occurrences of each character in string, and gives aDict and bDict
Iterate all the keys of bDict, if aDict.get(key, 0) is smaller than bDict[key], return False
Otherwise, return True outside the iteration

'''

class Solution:
	def compareStrings(self, A, B):
		aDict, bDict = self.stringStat(A), self.stringStat(B)
		for char in bDict.keys():
			if aDict.get(char, 0) < bDict[char]:
				return False
		return True

	def stringStat(self, string):
		statDict = dict()
		for char in string:
			statDict[char] = statDict.get(char, 0) + 1
		return statDict

A = 'ABCD'
B = 'ACD'

A = 'ABCD'
B = 'AABC'

inst = Solution()
print(inst.compareStrings(A, B))