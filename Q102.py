class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def hasCycle(self, head):
		if not head:
			return False
		fast, slow = head, head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return True
		return False

nums = [-21, 10, 4, 5, 3, 9]
lst = [ListNode(n) for n in nums]
for i in range(len(nums) - 1):
	lst[i].next = lst[i + 1]
lst[-1].next = lst[1]

head = lst[0]

inst = Solution()
print(inst.hasCycle(head))
