class Solution:
	def evaluateExpression(self, expression):
		expression = self.convertToRPN(expression)
		stack = []
		for char in expression:
			if char.isdigit():
				stack.append(int(char))
			else:
				b = stack.pop()
				a = stack.pop()
				if char == '+':
					c = a + b
				elif char == '-':
					c = a - b
				elif char == '*':
					c = a * b
				else:
					c = a // b
				stack.append(c)
		if stack:
			return stack[-1]
		return 0


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

expression = ['2', '*', '6', '-', '(', '23', '+', '7', ')', '/', '(', '1', '+', '2', ')']

inst = Solution()
print(inst.convertToRPN(expression))
print(inst.evaluateExpressions(expression))
