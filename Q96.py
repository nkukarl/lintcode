class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def partition(self, head, x):
		dummy = ListNode(x - 1, head)
		prevS = dummy
		slow = dummy.next
		while slow:
			while slow:
				if slow.val < x:
					prevS = prevS.next
					slow = slow.next
				else:
					break
			if not slow:
				return dummy.next
			prevF = slow
			fast = slow.next
			while fast:
				if fast.val >= x:
					prevF = prevF.next
					fast = fast.next
				else:
					break
			if not fast:
				return dummy.next
			tmp = fast.next
			prevS.next = fast
			prevS = fast
			fast.next = slow
			prevF.next = tmp

		return dummy.next

nums = [1, 4, 3, 2, 5, 2, 2, 3, 4]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
head = inst.partition(head, 3)

node = head
while node:
	print(node.val)
	node = node.next