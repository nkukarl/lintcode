class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def rotateRight(self, head, k):
		if not head:
			return None
		n = self.getLength(head)
		k %= n
		if k == 0:
			return head
		node = head
		while n - k - 1:
			node = node.next
			n -= 1
		newHead = node.next
		node.next = None

		node = newHead
		prev = None
		while node:
			prev = node
			node = node.next
		prev.next = head

		return newHead

	def getLength(self, head):
		n = 0
		while head:
			head = head.next
			n += 1
		return n

nums = [1, 2, 3, 4, 5]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.rotateRight(head, 7)

while head:
	print(head.val, end = ' ')
	head = head.next
print()
