'''
Thoughts:

Use two stacks to store the numbers coming in and current minimum
When a number comes in, it is appended to stack
For minStack, the incoming number is compared with the top of minStack, the smaller one will be appended to minStack
When popping out the numbers, remember to pop both stack and minStack
When peeking for min, return the top of minStack

'''

class MinStack:
	def __init__(self):
		self.stack = []
		self.minStack = []

	def push(self, number):
		self.stack.append(number)
		if not self.minStack:
			self.minStack = [number]
		else:
			self.minStack.append(min(self.minStack[-1], number))

	def pop(self):
		self.minStack.pop()
		return self.stack.pop()

	def min(self):
		return self.minStack[-1]

inst = MinStack()
inst.push(1)
print(inst.pop())
inst.push(2)
inst.push(3)
print(inst.min())
inst.push(1)
print(inst.min())