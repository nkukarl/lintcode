class DirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	def topSort(self, graph):
		graphCopy = graph[:]
		for node in graph:
			for n in node.neighbors:
				if n in graphCopy:
					graphCopy.remove(n)

		head = graphCopy[0]
		self.graph = graph[:]
		self.graph.remove(head)
		self.res = [[head]]
		self.helper(head, 1)

		ans = []
		for r in self.res:
			ans += r

		return ans

	def helper(self, node, level):
		# print('res:', self.res, 'level:', level)
		if self.graph:
			for n in node.neighbors:
				if n in self.graph:
					if len(self.res) <= level:
						self.res.append([n])
					else:
						self.res[level].append(n)
					self.graph.remove(n)
					self.helper(n, level + 1)

node0 = DirectedGraphNode(0)
node1 = DirectedGraphNode(1)
node2 = DirectedGraphNode(2)
node3 = DirectedGraphNode(3)
node4 = DirectedGraphNode(4)
node5 = DirectedGraphNode(5)

node0.neighbors = [node1, node2, node3]
node1.neighbors = [node4]
node2.neighbors = [node4, node5]
node3.neighbors = [node4, node5]

graph = [node0, node1, node2, node3, node4, node5]

inst = Solution()
for n in inst.topSort(graph):
	print(n.label, end = ' ')
print()