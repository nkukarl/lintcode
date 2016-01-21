class Solution:
	def convertToRPN(self, expression):
		output, stack = [], []
		precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
		for char in expression:
			if char.isdigit():
				output.append(char)
			elif char == '(':
				stack.append(char)
			elif char == ')':
				while stack and stack[-1] != '(':
					output.append(stack.pop())
				stack.pop()
			else:
				while stack and stack[-1] in precedence.keys() and precedence[char] <= precedence[stack[-1]]:
					output.append(stack.pop())
				stack.append(char)
		while stack:
			output.append(stack.pop())
		return output