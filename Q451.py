class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def swapPairs(self, head):
		dummy = ListNode(0)
		dummy.next = head
		prev = dummy
		node = head
		counter = 0
		k = 2
		while node:
			if counter != k - 1:
				node = node.next
				counter += 1
			else:
				next = node.next
				node.next = None
				HEAD, TAIL = self.reverse(prev.next)
				prev.next = HEAD
				prev = TAIL
				prev.next = next
				node = next
				counter = 0
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

nums = [1, 2, 3, 4, 5, 6]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.swapPairs(head)

while head:
	print(head.val, end = ' ')
	head = head.next
print()