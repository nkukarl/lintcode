'''
Thoughts:

Trivial

Initialise prev to None, cur to head
Iterate the list, store cur.next first
Set cur.next to prev, update prev to cur and then let cur = next

'''

class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def reverse(self, head):
		prev = None
		cur = head
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		return prev

nums = [n for n in range(1, 6)]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]

head = lst[0]

inst = Solution()
newHead = inst.reverse(head)

node = newHead
while node:
	print(node.val, end = ' ')
	node = node.next
print()