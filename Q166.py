class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def nthToLast(self, head, n):
		fast, slow = head, head
		while n:
			fast = fast.next
			n -= 1
		while fast:
			fast = fast.next
			slow = slow.next
		return slow

nums = [1, 3, 8, 11, 15]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
print(inst.nthToLast(head, 4).val)