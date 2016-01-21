class MyQueue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, element):
		self.stack1.append(element)

	def top(self):
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2[-1]

	def pop(self):
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()

inst = MyQueue()
inst.push(1)
print(inst.pop())
inst.push(2)
inst.push(3)
inst.push(4)
print(inst.top())
print(inst.pop())
print(inst.top())