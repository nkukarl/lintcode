class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def mergeKLists(self, lists):
		if not lists:
			return None
		head = lists[0]
		for h in lists[1:]:
			head = mergeList(head, h)
		return head

	def mergeList(self, head1, head2):
		if not head1:
			return head2
		if not head2:
			return head1
		dummy = ListNode(min(head1.val, head2.val) - 1)
		node = dummy
		while head1 and head2:
			if head1.val < head2.val:
				node.next = head1
				head1 = head1.next
			else:
				node.next = head2
				head2 = head2.next
			node = node.next
		if head1:
			node.next = head1
		else:
			node.next = head2
		return dummy.next

nums1 = [1, 3, 5, 8]
lst1 = [ListNode(n) for n in nums1]
for i in range(len(nums1) - 1):
	lst1[i].next = lst1[i + 1]
head1 = lst1[0]

nums2 = [2, 4, 6, 7, 9, 10]
lst2 = [ListNode(n) for n in nums2]
for i in range(len(nums2) - 1):
	lst2[i].next = lst2[i + 1]
head2 = lst2[0]	

inst = Solution()
head = inst.mergeList(head1, head2)

while head:
	print(head.val, end = ' ')
	head = head.next
print()

class Solution_opt:
	def mergeKLists(self, lists):
		if not lists:
			return None
		while len(lists) != 1:
			if len(lists) % 2 == 1:
				lists.append(None)
			tmp = []
			i = 0
			while i < len(lists) - 1:
				head1 = lists[i]
				head2 = lists[i + 1]
				tmp.append(self.mergeList(head1, head2))
				i += 2
			lists = tmp
		return lists[0]

	def mergeList(self, head1, head2):
		if not head1:
			return head2
		if not head2:
			return head1
		dummy = ListNode(min(head1.val, head2.val) - 1)
		node = dummy
		while head1 and head2:
			if head1.val < head2.val:
				node.next = head1
				head1 = head1.next
			else:
				node.next = head2
				head2 = head2.next
			node = node.next
		if head1:
			node.next = head1
		else:
			node.next = head2
		return dummy.next

# nums1 = [1, 3, 5, 8]
# lst1 = [ListNode(n) for n in nums1]
# for i in range(len(nums1) - 1):
# 	lst1[i].next = lst1[i + 1]
# head1 = lst1[0]

# nums2 = [2, 4, 6, 7, 9, 10]
# lst2 = [ListNode(n) for n in nums2]
# for i in range(len(nums2) - 1):
# 	lst2[i].next = lst2[i + 1]
# head2 = lst2[0]


class Solution_opt:
	def mergeKLists(self, lists):
		if not lists:
			return None
		if len(lists) == 1:
			return lists[0]
		left = self.mergeKLists(lists[:len(lists) // 2])
		right = self.mergeKLists(lists[len(lists) // 2:])
		return self.mergeList(left, right)

	def mergeList(self, head1, head2):
		if not head1:
			return head2
		if not head2:
			return head1
		dummy = ListNode(min(head1.val, head2.val) - 1)
		node = dummy
		while head1 and head2:
			if head1.val < head2.val:
				node.next = head1
				head1 = head1.next
			else:
				node.next = head2
				head2 = head2.next
			node = node.next
		if head1:
			node.next = head1
		else:
			node.next = head2
		return dummy.next

head1 = None
head2 = ListNode(1)

inst = Solution_opt()
head = inst.mergeKLists([head1, head2])

while head:
	print(head.val, end = ' ')
	head = head.next
print()