'''
Thoughts:

Trivial

Use two pointers to point to the current head of each list
Compare the value of two current nodes, append the smaller one to node.next

Return dummy.next
'''
class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, h1, h2):
		if not h1:
			return h2
		if not h2:
			return h1
		dummy = ListNode(min(h1.val, h2.val))
		node = dummy
		while h1 and h2:
			if h1.val < h2.val:
				node.next = h1
				h1 = h1.next
			else:
				node.next = h2
				h2 = h2.next
			node = node.next
		if not h1:
			node.next = h2
		else:
			node.next = h1
		return dummy.next

nums1 = [1, 3, 8, 11, 15]
lst1 = [ListNode(n) for n in nums1]
for i in range(len(lst1) - 1):
	lst1[i].next = lst1[i + 1]
h1 = lst1[0]

nums2 = [2, 4, 6, 7]
lst2 = [ListNode(n) for n in nums2]
for i in range(len(lst2) - 1):
	lst2[i].next = lst2[i + 1]
h2 = lst2[0]

inst = Solution()
head = inst.mergeTwoLists(h1, h2)

while head:
	print(head.val, end = ' ')
	head = head.next
print()