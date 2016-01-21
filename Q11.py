class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def searchRange(self, root, k1, k2):
		self.res = []
		self.helper(root, k1, k2)
		return self.res

	def helper(self, root, k1, k2):
		if root:
			if root.val < k1:
				self.helper(root.right, k1, k2)
			elif root.val > k2:
				self.helper(root.left, k1, k2)
			else:
				self.helper(root.left, k1, k2)
				self.res += [root.val]
				self.helper(root.right, k1, k2)

nums = [20, 8, 22, 4, 12]
tree = [TreeNode(n) for n in nums]

root = tree[0]
tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].left = tree[3]
tree[1].right = tree[4]

inst = Solution()
print(inst.searchRange(root, 4, 12))