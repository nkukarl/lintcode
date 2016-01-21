class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def zigzagLevelOrder(self, root):
		self.res = []
		self.helper(root, 0)
		return self.res

	def helper(self, root, level):
		if root:
			if level >= len(self.res):
				self.res.append([root.val])
			else:
				if level % 2 == 0:
					self.res[level].append(root.val)
				else:
					self.res[level].insert(0, root.val)
			self.helper(root.left, level + 1)
			self.helper(root.right, level + 1)

t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

inst = Solution()
print(inst.zigzagLevelOrder(t1))