'''
Thoughts:

getLength() returns the length of current list, n
Run helper(head, n) in sortedListToBST() and helper() does all the heavy lifting
For helper(), special cases are
n == 0, return None
n == 1, get val of current head to create root using TreeNode class and return root
Otherwise, let mid = n // 2
nLeft and nRight are then equal to mid and n - mid - 1, respectively
Let prev and cur be None and head, initialise counter to 0, while counter < mid, update prev and cur to cur and cur.next, respectively

cur corresponds to the list node we would like to use to create the root, hence root = TreeNode(cur.val)
prev then points to the end of the left list, let prev.next = None to end the list
cur.next points to the head of the right list
Hence, headLeft = prev and headRight = cur.next
Recursively use helper(headLeft, nLeft) and helper(headRight, nRight) to get the left subtree and right subtree of root and assign them accordingly

Return root eventually

'''

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return

        n = self.getLength(head)
        return self.helper(head, n)

    def helper(self, head, n):
        if n <= 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        if n == 2:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
        mid = n // 2
        nLeft = mid
        nRight = n - mid - 1
        prev = None
        cur = head
        counter = 0
        while counter < mid:
            prev = cur
            cur = cur.next
            counter += 1
        prev.next = None
        headLeft = head
        headRight = cur.next
        root = TreeNode(cur.val)
        root.left = self.helper(headLeft, nLeft)
        root.right = self.helper(headRight, nRight)
        return root

    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

inst = Solution()
root = inst.sortedListToBST(lst)