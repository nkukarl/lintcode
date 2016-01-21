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