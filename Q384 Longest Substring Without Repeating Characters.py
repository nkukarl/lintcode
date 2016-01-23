'''
Thoughts:

Iterate through all the characters in s
If current char is not in temporary array, append current char
Else find the index of current char in the temporary and discard all the chars before it and itself, append current char
Keep monitoring the length of the temporary array

'''

class Solution:
	def lengthOfLongestSubstring(self, s):
		tmp = []
		maxLen = 0
		for char in s:
			if char not in tmp:
				tmp += [char]
			else:
				tmp = tmp[tmp.index(char) + 1:] + [char]
			maxLen = max(maxLen, len(tmp))
		return maxLen

class Solution_twoPointer:
	def lengthOfLongestSubstring(self, s):
		s = list(s)
		tmp = []
		maxLen = 0
		fast, slow = 0, 0
		for fast in range(len(s)):
			char = s[fast]
			if char not in tmp:
				tmp.append(char)
			else:
				while s[slow] != char:
					slow += 1
				tmp = s[slow + 1 : fast + 1]
				slow += 1
			maxLen = max(maxLen, len(tmp))
		return maxLen

s = 'abcabcbb'
# s = 'bbbbb'
s = 'aab'

inst = Solution_twoPointer()
print(inst.lengthOfLongestSubstring(s))

