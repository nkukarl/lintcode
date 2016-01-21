class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def addLists(self, h1, h2):
		if not h1:
			return h2
		if not h2:
			return h1

		head = h1
		prev = None
		carry = 0
		while h1 and h2:
			tmp = h1.val + h2.val + carry
			val = tmp % 10
			carry = tmp // 10
			h1.val = val
			prev = h1
			h1 = h1.next
			h2 = h2.next
		if h1:
			h = h1
		else:
			h = h2
		prev.next = h
		while h:
			tmp = h.val + carry
			val = tmp % 10
			carry = tmp // 10
			h.val = val
			prev = h
			h = h.next
		if carry:
			prev.next = ListNode(1)

		return head

nums1 = [1, 2, 3]
lst1 = [ListNode(n) for n in nums1]
for i in range(len(lst1) - 1):
	lst1[i].next = lst1[i + 1]
h1 = lst1[0]

nums2 = [9, 9, 9, 9]
lst2 = [ListNode(n) for n in nums2]
for i in range(len(lst2) - 1):
	lst2[i].next = lst2[i + 1]
h2 = lst2[0]

inst = Solution()
head = inst.addLists(h1, h2)

while head:
	print(head.val, end = '')
	head = head.next
print()