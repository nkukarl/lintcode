class ExpressionTreeNode:
	def __init__(self, symbol):
		self.symbol = symbol
		self.left, self.right = None, None

class Solution:
	def build(self, expression):
		rpn = self.convertToRPN(expression)
		stack = []
		ops = ['+', '-', '*', '/']
		for char in rpn:
			if char not in ops:
				stack.append(ExpressionTreeNode(char))
			else:
				root = ExpressionTreeNode(char)
				root.right = stack.pop()
				root.left = stack.pop()
				stack.append(root)
		if stack:
			return stack[-1]

	def convertToRPN(self, expression):
		output = []
		stack = []
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

expression = ['2', '*', '6', '-', '(', '23', '+', '7', ')', '/', '(', '1', '+', '2', ')']

inst = Solution()
print(inst.convertToRPN(expression))
inst.build(expression)