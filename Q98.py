class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def sortList(self, head):
		if not head:
			return None
		if self.getLength(head) == 1:
			return head
		left, right = self.split(head)
		L, R = self.sortList(left), self.sortList(right)
		head = self.merge(L, R)
		return head

	def split(self, head):
		n = self.getLength(head)
		if n <= 1:
			return (head, 0)
		counter = 0
		node = head
		while counter < n // 2 - 1:
			node = node.next
			counter += 1
		
		right = node.next
		node.next = None
		left = head
		return (left, right)
		
	def merge(self, head1, head2):
		if not head1:
			return head2
		if not head2:
			return head1
		node1, node2 = head1, head2
		dummy = ListNode(0)
		node = dummy
		while node1 and node2:
			if node1.val < node2.val:
				node.next = node1
				node1 = node1.next
			else:
				node.next = node2
				node2 = node2.next
			node = node.next
		if node1:
			node.next = node1
		else:
			node.next = node2
		return dummy.next

	def getLength(self, head):
		n = 0
		node = head
		while node:
			n += 1
			node = node.next
		return n

	def printList(self, head):
		if not head:
			print('empty')
		else:
			while head:
				print(head.val)
				head = head.next
			print()


import random

nums = [n for n in range(1, 50)]
random.shuffle(nums)
print(nums)
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.sortList(head)

node = head
while node:
	print(node.val, end = ' ')
	node = node.next
print()