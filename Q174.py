class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head, n):
		fast, slow = head, head
		while n:
			fast = fast.next
			n -= 1
		# print(fast.val)
		prev = None
		while fast:
			fast = fast.next
			prev = slow
			slow = slow.next
		if slow == head:
			return head.next
		prev.next = slow.next
		return head

nums = [1, 2, 3, 4, 5]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.removeNthFromEnd(head, 5)

while head:
	print(head.val, end = ' ')
	head = head.next
print()
