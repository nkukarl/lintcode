class Solution:
	def isValidParentheses(self, s):
		left = {'(': 1, '[': 2, '{': 3}
		right = {')': 1, ']': 2, '}': 3}
		stack = []
		for char in s:
			if char in left:
				stack.append(char)
			else:
				if not stack or right[char] != left[stack[-1]]:
					return False
				stack.pop()
		if stack:
			return False
		return True

parentheses = ['([])', '()', '()[]{}', '(]', '([)]']

inst = Solution()
for p in parentheses:
	print(p, inst.isValidParentheses(p))