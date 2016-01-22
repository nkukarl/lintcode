'''
Thoughts:

Iterate the chars in s:
If char is a left bracket, push it to the stack
If char is a right bracket, check
	whether the stack is empty: is empty -> False
	whether the top of the stack is a left bracket: not left -> False
	whether the left and right bracket match each other: not match -> False
Otherwise, pop the top element and continue

When the iteration finishes, the stack shall be empty if the parentheses are valid

'''

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