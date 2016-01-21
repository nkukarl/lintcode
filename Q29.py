class Solution:
	def isInterleave(self, s1, s2, s3):
		# print(s1, s2, s3)

		# s1, s2 and s3 all empty
		if s1 == s2 == s3 == '':
			return True
		# s3 empty, s1 not empty or s2 not empty
		if s3 == '':
			return False
		# s1 empty
		if not s1:
			return s2 == s3
		# s2 empty
		if not s2:
			return s1 == s3

		if len(s1) + len(s2) != len(s3):
			return False

		if s1[0] == s3[0] and s2[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
		if s1[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:])
		if s2[0] == s3[0]:
			return self.isInterleave(s1, s2[1:], s3[1:])

		return False

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'

s1, s2, s3 = 'aa', 'ab', 'abaa'

inst = Solution()
print(inst.isInterleave(s1, s2, s3))