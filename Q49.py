class Solution:
	def sortLetters(self, chars):
		i, j = 0, len(chars) - 1
		while i < j:
			while ord(chars[i]) >= ord('a') and ord(chars[i]) <= ord('z') and i < len(chars) - 1:
				i += 1
			while ord(chars[j]) >= ord('A') and ord(chars[j]) <= ord('Z') and j > 0:
				j -= 1
			if i < j:
				chars[i], chars[j] = chars[j], chars[i]
			i += 1
			j -= 1

chars = ['a', 'b', 'A', 'c', 'D']

# chars = ['D', 'E', 'R', 'L', 'K', 'A', 'J', 'K', 'F', 'K', 'L', 'A', 'J', 'F', 'K', 'A', 'K', 'L', 'F', 'J', 'K', 'L', 'J', 'F', 'a']

inst = Solution()
inst.sortLetters(chars)

print(chars)
