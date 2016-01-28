'''
Thoughts:

if s is empty, return
Mod offset by n = len(s)
Pivot is located at n - 1 - offset
Reverse elements from 0 to pivot (inclusive)
Reverse elements from pivot + 1 to end (inclusive)
Reverse entire s

'''

class Solution:
	def rotateString(self, s, offset):
		if not s:
			return
		n = len(s)
		offset %= n
		self.reverse(s, 0, n - 1 - offset)
		self.reverse(s, n - offset, n - 1)
		self.reverse(s, 0, n - 1)
	
	def reverse(self, s, start, end):
		while start < end:
			s[start], s[end] = s[end], s[start]
			start += 1
			end -= 1

inst = Solution()

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
inst.rotateString(s, 3)
print(s)