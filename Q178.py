class Solution:
	def validTree(self, n, edges):
		summary = [i for i in range(n)]
		for edge in edges:
			a, b = edge
			if a > b:
				a, b = b, a
			if summary[a] == summary[b]:
				return False
			tmp = []
			for i in range(len(summary)):
				if summary[i] == summary[a] or summary[i] == summary[b]:
					tmp.append(i)
			for t in tmp:
				summary[t] = b
			# print(summary)
		
		if len(set(summary)) == 1:
			return True
		return False

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [1, 3]]
edge = [[0, 1], [2, 4], [2, 3], [1, 4]]

inst = Solution()
print(inst.validTree(n, edges))
