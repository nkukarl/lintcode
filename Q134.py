class LRUCache:
	def __init__(self, capacity):
		self.keys = []
		self.values = []
		self.capacity = capacity

	def get(self, key):
		if key in self.keys:
			idx = self.keys.index(key)
			key = self.keys.pop(idx)
			self.keys.append(key)
			value = self.values.pop(idx)
			self.values.append(value)
			return self.values[self.keys.index(key)]
		return -1
		
	def set(self, key, value):
		# write your code here
		if key not in self.keys:
			self.keys.append(key)
			self.values.append(value)
			if len(self.keys) > self.capacity:
				self.keys.pop(0)
				self.values.pop(0)
		else:
			index = self.keys.index(key)
			self.keys.pop(index)
			self.values.pop(index)
			self.keys.append(key)
			self.values.append(value)


inst = LRUCache(2)

inst.set(2, 1)
inst.set(1, 1)
print(inst.get(2))
inst.set(4, 1)
print(inst.get(1))
print(inst.get(2))