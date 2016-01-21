class Solution:
	def minWindow(self, source, target):
		if not target or not self.helper(source, target):
			return ''
		fast, slow = 1, 0
		window = source
		while fast < len(source):
			while not self.helper(source[slow : fast], target) and fast < len(source):
				fast += 1
			while self.helper(source[slow : fast], target):
				slow += 1
				if len(source[slow - 1 : fast]) < len(window):
					window = source[slow - 1 : fast]
		return window

	def helper(self, s, t):
		sDict, tDict = {}, {}
		for char in s:
			sDict[char] = sDict.get(char, 0) + 1
		for char in t:
			tDict[char] = tDict.get(char, 0) + 1
		for char in tDict:
			if sDict.get(char, 0) < tDict[char]:
				return False
		return True

source = 'ABC'
target = 'AC'

inst = Solution()
print(inst.minWindow(source, target))

# print(inst.helper(source, target))