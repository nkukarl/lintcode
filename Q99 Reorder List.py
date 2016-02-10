'''
Thoughts:

merge() will merge two lists
reverse() will reverse a list

Use fast and slow to split the original list into two, reverse the second list and then return the merged first and second list
'''

class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def reorderList(self, head):
		if not head or not head.next or not head.next.next:
			return head
		slow, fast = head, head

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		headB = slow.next
		slow.next = None
		headA = head

		headB = self.reverse(headB)
		return self.merge(headA, headB)


	def merge(self, headA, headB):
		dummy = ListNode(0)
		node = dummy
		while headA and headB:
			node.next = headA
			headA = headA.next
			node = node.next
			node.next = headB
			headB = headB.next
			node = node.next
		if headA:
			node.next = headA
		else:
			node.next = headB

		return dummy.next
	
	def reverse(self, head):
		prev = None
		cur = head
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		return prev

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