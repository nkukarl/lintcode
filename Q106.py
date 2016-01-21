class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def sortedListToBST(self, head):
		return self.helper(head, self.getLength(head))

	def helper(self, head, n):
		if not head:
			return None
		if n == 1:
			return TreeNode(head.val)
		if n == 2:
			root = TreeNode(head.val)
			root.right = TreeNode(head.next.val)
			return root
		counter = 0
		node = head
		while counter < (n - 1) // 2 - 1:
			node = node.next
			counter += 1
		# print(counter)

		tmp = node.next
		root = TreeNode(tmp.val)
		node.next = None
		# print('root', end = ' ')
		# print(tmp.val)
		# print('left', end = ' ')
		# self.printList(head)
		# print('right', end = ' ')
		# self.printList(tmp.next)
		root.left = self.helper(head, counter + 1)
		root.right = self.helper(tmp.next, n - counter - 2)

		return root
	
	def getLength(self, head):
		n = 0
		while head:
			n += 1
			head = head.next
		return n

	def printList(self, head):
		if not head:
			print('None')
		else:
			while head:
				print(head.val, end = ' ')
				head = head.next
			print()


# lst = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

# lst = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

lst = ListNode(-1, ListNode(0, ListNode(1, ListNode(3, ListNode(4, ListNode(5))))))

inst = Solution()
inst.sortedListToBST(lst)