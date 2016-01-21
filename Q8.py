class Solution:
	def rotateString(self, s, offset):
		if len(s) >= 2:

			offset %= len(s)

			pivot = len(s) - offset

			i, j = 0, pivot - 1
			while j - i >= 1:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1

			i, j = pivot, len(s) - 1
			while j - i >= 1:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1

			i, j = 0, len(s) - 1
			while j - i >= 1:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1

inst = Solution()

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
inst.rotateString(s, 3)
print(s)