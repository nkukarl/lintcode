'''
Thoughts:

getLength() returns the length of each list
discard the first several nodes of the longer list so that the two list have identical length
Iterate the nodes in the two lists and compare the value of two nodes

'''

class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def getIntersectionNode(self, headA, headB):
		if not headA or not headB:
			return None

		lenA, lenB = self.getLength(headA), self.getLength(headB)
		if lenA < lenB:
			headA, headB = headB, headA
		diff = abs(lenA - lenB)
		while diff:
			headA = headA.next
			diff -= 1
		while headA:
			if headA == headB:
				return headA
			headA = headA.next
			headB = headB.next
		return None

	def getLength(self, head):
		counter = 0
		while head:
			counter += 1
			head = head.next
		return counter

lst = [ListNode(n) for n in range(1, 5)]
for i in range(len(lst) - 1):
	lst[i].next = lst[i + 1]
headA = lst[0]
headB = lst[2]

inst = Solution()
inst.getIntersectionNode(headA, headB)