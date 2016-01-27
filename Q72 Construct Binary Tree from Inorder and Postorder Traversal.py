'''
Thoughts:

If a tree is like

    1
   / \
  2   3
 / \ / \
4   56  7

Inorder traversal shall return inorder = [4, 2, 5, 1, 6, 3, 7]
Postorder traversal shall return postorder = [4, 5, 2, 6, 7, 3, 1]

If inorder or postorder is empty, return None
The last number in postorder shall go to the root, locate this element in inorder, mark is position as pos
In postorder, index 1 to pos - 1 (inclusive) shall go to postorderLeft, index pos to end - 1 shall go to postorderRight
inorderLeft and postorderLeft shall form the left of current root
In inorder, index 1 to pos - 1(inclusive) shall go to inorderLeft, index pos + 1 to the end shall go to inorderRight
inorderRight and postorderRight shall form the right of current root

return root

'''

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def buildTree(self, inorder, postorder):
		if postorder:
			val = postorder[-1]
			root = TreeNode(val)
			pos = inorder.index(val)
			root.left = self.buildTree(inorder[:pos], postorder[:pos])
			root.right = self.buildTree(inorder[pos + 1:], postorder[pos: -1])
			return root

inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

inst = Solution()
root = inst.buildTree(inorder, postorder)