class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def reorderList(self, head):
		n = self.getLength(head)
		if n <= 0:
			return head
		node = head	
		counter = 0
		while counter < (n - 1) // 2:
			counter += 1
			node = node.next
		right = node.next
		node.next = None
		left = head
		right = self.reverse(right)
		head = self.merge(left, right)
		return head

	def reverse(self, head):
		if head:
			prev = None
			node = head
		while node:
			next = node.next
			node.next = prev
			prev = node
			node = next
		return prev

	def merge(self, head1, head2):
		dummy = ListNode(0)
		node = dummy
		while head2:
			node.next = head1
			node = node.next
			head1 = head1.next
			node.next = head2
			node = node.next
			head2 = head2.next
		node.next = head1
		return dummy.next

	def getLength(self, head):
		n = 0
		while head:
			n += 1
			head = head.next
		return n

import random

nums = [1, 2, 3, 4, 5]
# nums = [n for n in range(1, 5)]
# random.shuffle(nums)
# print(nums)
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.reorderList(head)
node = head
while node:
	print(node.val, end = ' ')
	node = node.next
print()