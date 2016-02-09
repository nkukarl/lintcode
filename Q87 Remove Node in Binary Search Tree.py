'''
Thoughts:

If root is None, the value cannot be found in the tree, return root
Otherwise, compare root.val to value

If root.val == value, the root shall be removed from the tree
We can either keep the left child, and append the right child to the left child or keep the right child and append the left child to the right child
Here we choose to use the 2nd implementation
If root.right is None, return root.left
Otherwise, let tmp = root.left, let tmp be the left child of the leftmost node in the right child, return root.right

If root.val < value, the node that needs to be removed might exist in the right tree of root, hence root.right = self.removeNode(root.right, value)
Otherwise, root.left = self.removeNode(root.left, value)
Return root



'''

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def removeNode(self, root, value):
		if not root:
			return root
		if root.val == value:
			if not root.right:
				return root.left
			tmp = root.left
			cur = root.right
			prev = None
			while cur:
				prev = cur
				cur = cur.left
			prev.left = tmp
			return root.right

		if root.val < value:
			root.right = self.removeNode(root.right, value)
		else:
			root.left = self.removeNode(root.left, value)
		return root

nums = [5, 3, 6, 2, 4]
tree = [TreeNode(n) for n in nums]

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].left = tree[3]
tree[1].right = tree[4]
root = tree[0]

value = 1

inst = Solution()
newRoot = inst.removeNode(root, value)