class DirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	def hasRoute(self, graph, s, t):
		if not graph:
			return False
		self.visited = set()
		return self.helper(s, t)

	def helper(self, s, t):
		if t == s:
			return True
		self.visited.add(s)
		for n in s.neighbors:
			if n not in self.visited:
				if self.helper(n, t):
					return True

		return False


labels = ['A', 'B', 'C', 'D', 'E']
graph = [DirectedGraphNode(char) for char in labels]
graph[0].neighbors = [graph[0], graph[3]]
graph[1].neighbors = [graph[2], graph[3]]
graph[3].neighbors = [graph[4]]

s, t = graph[1], graph[4]
# s, t = graph[3], graph[2]

inst = Solution()
print(inst.hasRoute(graph, s, t))