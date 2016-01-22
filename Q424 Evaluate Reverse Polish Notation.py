'''
Thoughts:

Iterate the tokens:
If token is a number, push it to the stack
If token is an operator, pop the top two numbers, perform calculation and push the result back to the stack
Pop the last element when the iteration ends
If stack is empty, RPN is valid, return the final result

Be careful '-X'.isdigit() returns False
use try and except instead

'''

class Solution:
	def evalRPN(self, tokens):
		stack = []
		for t in tokens:
			try:
				stack.append(int(t))
			except:
				num2 = stack.pop()
				num1 = stack.pop()
				if t == '+':
					num = num1 + num2
				elif t == '-':
					num = num1 - num2
				elif t == '*':
					num = num1 * num2
				else:
					if num1 * num2 > 0:
						sign = 1
					else:
						sign = -1
					num = abs(num1) // abs(num2) * sign
				stack.append(num)
		res = stack.pop()
		if not stack:
			return res

tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["3", "-4", "+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

inst = Solution()
print(inst.evalRPN(tokens))