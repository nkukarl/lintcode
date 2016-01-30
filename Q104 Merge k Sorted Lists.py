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



'''
Thoughts:

Recursively split lists into two sublists
If a sublist has only one element, directly return the element
Use mergeList to merge two lists and return the merged list recursively

'''
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


'''
Thoughts:

Similar to Q401 Kth Smallest Number in Sorted Matrix

Since each list has been sorted, for each non-empty list, it shall be pushed to mh (an instance of MinHeap)
While mh is not empty, pop the root element and denote it as tmp
Append tmp to the new list, starts with dummy
If tmp.next is not None, push tmp.next to mh
Return dummy.next

'''

# class ListNode(object):
#     def __init__(self, val, next = None):
#         self.val = val
#         self.next = next

class MinHeap:
    def __init__(self):
        self.A = []

    def push(self, element):
        self.A.append(element)
        self.__up(len(self.A) - 1)

    def __up(self, i):
        if i <= 0:
            return
        parentId = (i - 1) // 2
        if self.A[i].val < self.A[parentId].val:
            self.A[i], self.A[parentId] = self.A[parentId], self.A[i]
            self.__up(parentId)

    def pop(self):
        if not self.A:
            return
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        tmp = self.A.pop()
        self.__down(0)
        return tmp

    def __down(self, i):
        if i >= len(self.A):
            return
        leftId, rightId = 2 * i + 1, 2 * i + 2
        if leftId >= len(self.A):
            left = 2 ** 31
        else:
            left = self.A[leftId].val
        if rightId >= len(self.A):
            right = 2 ** 31
        else:
            right = self.A[rightId].val
        if left < right and left < self.A[i].val:
            self.A[i], self.A[leftId] = self.A[leftId], self.A[i]
            self.__down(leftId)
        elif right < self.A[i].val:
            self.A[i], self.A[rightId] = self.A[rightId], self.A[i]
            self.__down(rightId)

    def top(self):
        if self.A:
            return self.A[0]

class Solution:
    def mergeKLists(self, lists):
        mh = MinHeap()
        for l in lists:
            if l:
                mh.push(l)

        dummy = ListNode(0)
        node = dummy

        while mh.top():
            tmp = mh.pop()
            node.next = tmp
            node = node.next
            if node.next:
                mh.push(node.next)

        return dummy.next

lists = [
ListNode(0, ListNode(2, ListNode(4))),
ListNode(-1, ListNode(3, ListNode(7))),
ListNode(-1, ListNode(3.5, ListNode(5))),
None,
ListNode(100),
ListNode(27)
]

inst = Solution()
head = inst.mergeKLists(lists)

while head:
    print(head.val, end = ' ')
    head = head.next
print()