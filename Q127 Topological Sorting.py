'''
Thoughts:

Use self.visited and self.stack to store the visited nodes and nodes that have been thoroughly explored
A node that has been thoroughly explored means all the neighbors of the node as well as the neighbors of it neighbors have been visited

helper() then applies this DFS algorithm, if node has been visited, exit helper()
Otherwise, add node to self.visited and explore its neighbors using helper()
Append node to stack after it has been completed explored (at the end of helper())

Reverse self.stack and return it

'''
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def topSort(self, graph):
        self.visted = set()
        self.stack = []

        for n in graph:
            self.helper(n)

        self.stack.reverse()
        return self.stack

    def helper(self, n):
        if n not in self.visted:
            self.visted.add(n)
            for nb in n.neighbors:
                self.helper(nb)
            self.stack.append(n)

graph = [DirectedGraphNode(i) for i in range(6)]
graph[0].neighbors = [graph[1], graph[2], graph[3]]
graph[1].neighbors = [graph[4]]
graph[2].neighbors = [graph[4], graph[5]]
graph[3].neighbors = [graph[4], graph[5]]

inst = Solution()
graph = inst.topSort(graph)

for i in range(len(graph)):
    print(graph[i].label)