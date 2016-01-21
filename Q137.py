class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	def cloneGraph(self, node):
		if not node:
			return node
		copyNode = UndirectedGraphNode(node.label)
		stack = []
		MAP = {node.label: copyNode}
		stack.append(node)
		while stack:
			top = stack.pop()
			cur = MAP[top.label]
			for n in top.neighbors:
				if n.label not in MAP:
					MAP[n.label] = UndirectedGraphNode(n.label)
					stack.append(n)
				cur.neighbors.append(MAP[n.label])
		return copyNode