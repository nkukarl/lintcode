'''
Thoughts:

If a tree is like

    1
   / \
  2   3
 / \ / \
4   56  7

Preorder traversal shall return preorder = [1, 2, 4, 5, 3, 6, 7]
Inorder traversal shall return inorder = [4, 2, 5, 1, 6, 3, 7]

If preorder or inorder is empty, return None
The first number in preorder shall go to the root, locate this element in inorder, mark is position as pos
In preorder, index 1 to pos (inclusive) shall go to preorderLeft, index pos + 1 to the end shall go to preorderRight
preorderLeft and inorderLeft shall form the left of current root
In inorder, index 1 to pos - 1(inclusive) shall go to inorderLeft, index pos + 1 to the end shall go to inorderRight
preorderRight and inorderRight shall form the right of current root

return root

'''

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def buildTree(self, preorder, inorder):
		if preorder:
			val = preorder[0]
			root = TreeNode(val)
			pos = inorder.index(val)
			root.left = self.buildTree(preorder[1 : pos + 1], inorder[:pos])
			root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
			return root

preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]

inst = Solution()
root = inst.buildTree(preorder, inorder)