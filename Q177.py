class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None
		mid = (len(nums) - 1) // 2
		root = TreeNode(nums[mid])
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid + 1:])
		return root

nums = [1, 2, 3, 4, 5, 6, 7]

inst = Solution()
root = inst.sortedArrayToBST(nums)

