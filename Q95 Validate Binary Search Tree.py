'''
Thoughts:

Let MAX and MIN be the default upper and lower limit

If not root, return True since an empty tree is a valid BST

If root.val <= MIN or root.val >= MAX, return False
Otherwise, check whether the left and right subtree of the current root is a valid BST
The upper and lower limit of the left subtree is then root.val and MIN
The upper and lower limit of the right subtree is then MAX and root.val

'''
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def isValidBST(self, root):
		MAX = 2 ** 31
		MIN = -2 ** 31 - 1
		return self.helper(root, MIN, MAX)

	def helper(self, root, MIN, MAX):
		if not root:
			return True
		if root.val <= MIN or root.val >= MAX:
			return False
		return self.helper(root.left, MIN, root.val) and self.helper(root.right, root.val, MAX)


nums = [2, 1, 4, 3, 5]
tree = [TreeNode(n) for n in nums]

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[2].left = tree[3]
tree[2].right = tree[4]

root = tree[0]

inst = Solution()
print(inst.isValidBST(root))