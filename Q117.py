class Solution:
	def jump(self, A):
		steps = 1
		left, right = 0, A[0]
		tmp = 0
		while right < len(A) - 1:
			steps += 1
			for pos in range(left, right + 1):
				tmp = max(tmp, pos + A[pos])
			left = right
			right = tmp
		return steps


A = [2, 3, 1, 1, 4]
# A = [3, 2, 1, 0, 4]
# A = [1, 0]

inst = Solution()
print(inst.jump(A))