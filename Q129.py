class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def rehashing(self, hashTable):
		size = len(hashTable)
		newSize = size * 2
		newTable = [None] * newSize
		
		for lst in hashTable:
			while lst:
				pos = lst.val % newSize
				if newTable[pos]:
					head = newTable[pos]
					while head.next:
						head = head.next
					head.next = ListNode(lst.val)
				else:
					newTable[pos] = ListNode(lst.val)
				lst = lst.next
		return newTable

hashTable = [None, ListNode(21, ListNode(9)), ListNode(14), None]

inst = Solution()
newTable = inst.rehashing(hashTable)

