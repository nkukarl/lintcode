'''
Thoughts:

Let connect be the array recording how the nodes are connected
connect has a size of n and for each element, its index represents the starting node and its value represents the ending node
Initially, connect = [1, 2, 3, ..., n - 2, n - 1] since we are assuming each node is not connected to another node
Since there are no duplicate edges and edge [a, b] and [b, a] will only appear once in edges, let us say [a, b] will appear in edges
Iterate all the edges, if connect[a] is already equal to connect[b] before edge [a, b] is processed, then it means there are more than one route between node a and b, which means the tree is not valid
Otherwise, we shall mark all the elements in connect whose value is a into b
Use tmp to store connect[a] and iterate all the elements in connect and compare connect[i] to tmp to achieve this.

After iterating all the edges, the number of unique values in connect represents the number of trees, if len(set(connect)) is 1, then the tree is valid, otherwise, it is not valid

'''

class Solution:
	def validTree(self, n, edges):
		connect = [i for i in range(n)]
		for edge in edges:
			a, b = edge
			if connect[a] == connect[b]:
				return False
			tmp = connect[a]
			for i in range(len(connect)):
				if connect[i] == tmp:
					connect[i] = connect[b]

		return len(set(connect)) == 1

