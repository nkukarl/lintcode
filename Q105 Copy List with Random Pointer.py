'''
Thoughts:

Iterate all the nodes in the list, insert a duplicate node between current node and next node
Take list 2 -> 3 -> 4 -> 7 -> 8 as an example, we would have
2 -> 2 -> 3 -> 3 -> 4 -> 4 -> 7 -> 7 -> 8 -> 8
N.B. the random pointer has not be dealt with

Then let node = head, iterate all the nodes in the original list
If node.random, let node.next.random = node.random.next
node = node.next.next so that we could skip those duplicated nodes

Then split the current list into 2
Let HEAD = node.next and let node = head, NODE = HEAD
While NODE.next (the list has not been iterated till the end), let
node.next = NODE.next and NODE.next = NODE.next.next
Update node and NODE to their next at the end of each iteration

Do not forget to update node.next to None outside the iteration

Return HEAD, which is a deep copy of list accessed from head

'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        node = head
        while node:
            NEXT = node.next
            node.next = RandomListNode(node.label)
            node.next.next = NEXT
            node = NEXT

        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        node = head
        HEAD = node.next
        NODE = HEAD

        while NODE.next:
            node.next = NODE.next
            NODE.next = NODE.next.next
            node = node.next
            NODE = NODE.next

        node.next = None

        return HEAD

nums = [2, 3, 4, 7, 8]
lst = [RandomListNode(n) for n in nums]
for i in range(len(lst) - 1):
    lst[i].next = lst[i + 1]
lst[1].random = lst[0]
lst[2].random = lst[4]
head = lst[0]

inst = Solution()
head = inst.copyRandomList(head)

while head:
    print(head.label, end = ' ')
    head = head.next
print()