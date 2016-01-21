class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

# class Solution:
# 	def insertionSortList(self, head):
# 		if not head:
# 			return None
# 		dummy = ListNode(-2 ** 32)
# 		nodeIns = head
# 		while nodeIns:
# 			prev = None
# 			node = dummy
# 			while node and nodeIns.val > node.val:
# 				prev = node
# 				node = node.next

# 			prev.next = nodeIns
# 			next = nodeIns.next
# 			nodeIns.next = node
# 			nodeIns = next

# 		return dummy.next

class Solution_opt:
	def insertionSortList(self, head):
		if not head:
			return None
		dummy = ListNode(-2 ** 32, head)
		last = dummy

		nodeIns = head
		while nodeIns:
			if nodeIns.val > last.val:
				last.next = nodeIns
				last = nodeIns
				tmp = nodeIns.next
				nodeIns.next = None
				nodeIns = tmp
			else:
				tmp = nodeIns.next
				nodeIns.next = None
				self.insert(dummy, nodeIns)
				nodeIns = tmp

		return dummy.next


	def insert(self, head, node):
		prev = head
		cur = head.next
		while cur and node.val > cur.val:
			prev = cur
			cur = cur.next
		prev.next = node
		node.next = cur




# nums = [6, 2, 1, 3, 4]
# lst = [ListNode(n) for n in nums]
# for i in range(len(lst) - 1):
# 	lst[i].next = lst[i + 1]
# head = lst[0]
# node = ListNode(7)

head = ListNode(6, ListNode(2, ListNode(1, ListNode(3, ListNode(4)))))

inst = Solution_opt()
head = inst.insertionSortList(head)

while head:
	print(head.val, end = ' ')
	head = head.next
print()