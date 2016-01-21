class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def reverseBetween(self, head, m, n):
		if m == n:
			return head
		dummy = ListNode(0, head)
		i = -1
		node = dummy
		for i in range(m - 1):
			node = node.next
		pos1 = node
		reverseHead = node.next
		for j in range(i + 1, n - 1):
			node = node.next
		reverseTail = node.next
		pos2 = reverseTail.next
		reverseTail.next = None

		newHead, newTail = self.reverse(reverseHead)
		pos1.next = newHead
		newTail.next = pos2

		return dummy.next

	def reverse(self, head):
		prev = None
		cur = head
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		
		HEAD, TAIL = prev, head
		return (HEAD, TAIL)

nums = [n for n in range(1, 10)]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]

head = lst[0]

inst = Solution()
newHead = inst.reverseBetween(head, 1, 9)

node = newHead
while node:
	print(node.val, end = ' ')
	node = node.next
print()