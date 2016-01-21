class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def removeElements(self, head, val):
		dummy = ListNode(val - 1)
		dummy.next = head
		prev = dummy
		cur = dummy.next
		while cur:
			if cur.val != val:
				prev = cur
				cur = cur.next
			else:
				cur = cur.next
				prev.next = cur
		return dummy.next

nums = [1, 2, 3, 3, 4, 5, 3]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.removeElements(head, 2)

while head:
	print(head.val, end = ' ')
	head = head.next
print()