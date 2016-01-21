class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	def copyRandomList(self, head):
		if not head:
			return None
		node = head
		while node:
			next = node.next
			copyNode = RandomListNode(node.label)
			node.next = copyNode
			copyNode.next = next
			node = next

		node1, node2 = head, head.next
		while node2:
			if node1.random:
				node2.random = node1.random.next
			node1 = node1.next.next
			if node2.next:
				node2 = node2.next.next
			else:
				node2 = None
		
		copyHead = head.next
		node1, node2 = head, head.next
		while node1:
			tmp = node2.next
			if tmp:
				node2.next = tmp.next
				node1.next = tmp
				node1 = tmp
				node2 = tmp.next
			else:
				node1.next = None
				node1 = None

		return copyHead



nums = [-1, 8, 7, -3, 4]
lst = [RandomListNode(n) for n in nums]
for i in range(len(nums) - 1):
	lst[i].next = lst[i + 1]
head = lst[0]
lst[0].random = lst[4]
lst[1].random = lst[3]
lst[4].random = lst[0]

inst = Solution()
head = inst.copyRandomList(head)

while head:
	print(head.label, end = ' ')
	if head.random:
		print(head.random.label)
	else:
		print('None')
	head = head.next
print()