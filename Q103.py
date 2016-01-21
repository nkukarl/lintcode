class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def detectCycle(self, head):
		if not head:
			return False
		fast, slow = head, head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				print(fast.val)
				pos = head
				while head != slow:
					head = head.next
					slow = slow.next
				return slow
		return None

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [ListNode(n) for n in nums]
for i in range(len(nums) - 1):
	lst[i].next = lst[i + 1]
lst[-1].next = lst[1]

head = lst[0]

inst = Solution()
print(inst.detectCycle(head).val)
