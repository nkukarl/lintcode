class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def isPalindrome(self, head):
		if not head:
			return True
		fast, slow = head, head
		prev = None
		while fast and fast.next:
			fast = fast.next.next
			prev = slow
			slow = slow.next
		if not prev:
			return True
		head1 = head
		head2 = prev.next
		prev.next = None

		head2 = self.reverse(head2)

		while head1:
			if head1.val != head2.val:
				return False
			head1 = head1.next
			head2 = head2.next
		return True

	def reverse(self, head):
		if not head:
			return None
		prev = None
		cur = head
		node = head
		while node:
			next = node.next
			node.next = prev
			prev = node
			node = next
		return prev

nums = [1, 0, 3, 4, 0, 1]
# nums = [1, 2, 3, 3, 2, 1]
# nums = [1, 2, 3, 2, 1]
nums = [1, 2, 1]
lst = [ListNode(n) for n in nums]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]

inst = Solution()
print(inst.isPalindrome(head))