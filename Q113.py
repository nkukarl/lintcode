class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def deleteDuplicates(self, head):
		if not head:
			return None
		dummy = ListNode(head.val - 1, head)
		cur = dummy.next
		prev = dummy
		while cur:
			if cur.val != prev.val:
				if not cur.next or cur.next.val != cur.val:
					prev = cur
					cur = cur.next
				else:
					curVal = cur.val
					while cur and cur.val == curVal:
						cur = cur.next
					prev.next = cur
			else:
				curVal = cur.val
				while cur and cur.val == curVal:
					cur = cur.next
				prev.next = cur

		return dummy.next

nums = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 6]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.deleteDuplicates(head)

while head:
	print(head.val, end = ' ')
	head = head.next
print()
