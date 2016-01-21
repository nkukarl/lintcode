class Solution:
	def canJump(self, A):
		pos = A[0]
		for i in range(1, len(A)):
			if i <= pos:
				pos = max(pos, i + A[i])
			if pos >= len(A) - 1:
				return True
		return False

# A = [2, 3, 1, 1, 4]
# A = [3, 2, 1, 0, 4]
A = [1, 0]

inst = Solution()
print(inst.canJump(A))