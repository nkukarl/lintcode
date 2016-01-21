'''
Thoughts:

dfs problem
If right < left, the current generated parenthesis is invalid
Use the numbers of left and right bracket allowed as indicators
If both right and left are zero, append current generated parenthesis to the result
Otherwise, enter next level recursion

'''
class Solution:
	def generateParenthesis(self, n):
		self.res = []
		self.helper(n, n, '')
		return self.res

	def helper(self, left, right, cur):
		if right < left:
			return
		if left == right == 0:
			self.res += [cur]
		if left > 0:
			self.helper(left - 1, right, cur + '(')
		if right > 0:
			self.helper(left, right - 1, cur + ')')

n = 3

inst = Solution()
print(inst.generateParenthesis(n))