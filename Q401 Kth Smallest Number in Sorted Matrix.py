'''
Thoughts:

Define MinHeap class with push(), pop() and top() methods
push() will add new elements to mh (instance of MinHeap) and update the elements in mh to make it remain valid using __up()
pop() will remove the root element of mh and update the elements in mh to make it remain valid using __down()
top() returns the root element

Let m and n denote the row and column number of matrix
Add values, together with corresponding row and column indices, in the first row of the matrix to mh
Repeat the following k - 1 times since we only need to pop() k - 1 elements from mh and then peek the root to get the kth smallest
Get the root of current mh using pop()
if root[1] (row index) is less than m - 1, it means the for the current column, element in matrix[row + 1][col] has not been added to mh, thus push the value together with corresponding row and column indices to mh
Otherwise, the current column has been depleted, enter another iteration by popping out the root of mh

Get the root of current mh using top() and return root[0]

'''

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
        if self.A[i][0] < self.A[parentId][0]:
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
            left = self.A[leftId][0]
        if rightId >= len(self.A):
            right = 2 ** 31
        else:
            right = self.A[rightId][0]
        if left < right and left < self.A[i][0]:
            self.A[i], self.A[leftId] = self.A[leftId], self.A[i]
            self.__down(leftId)
        elif right < self.A[i][0]:
            self.A[i], self.A[rightId] = self.A[rightId], self.A[i]
            self.__down(rightId)

    def top(self):
        return self.A[0]


class Solution:
    def kthSmallest(self, matrix, k):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        if k > m * n:
            return

        mh = MinHeap()

        for col in range(n):
            mh.push((matrix[0][col], 0, col))

        while k - 1:
            val, row, col = mh.pop()
            if row < m - 1:
                mh.push((matrix[row + 1][col], row + 1, col))

            k -= 1

        root = mh.top()
        return root[0]

matrix = [[1, 5, 7], [3, 7, 8], [4, 8, 9]]

inst = Solution()
print(inst.kthSmallest(matrix, 1))
print(inst.kthSmallest(matrix, 2))
print(inst.kthSmallest(matrix, 3))
print(inst.kthSmallest(matrix, 4))
print(inst.kthSmallest(matrix, 5))
print(inst.kthSmallest(matrix, 6))
print(inst.kthSmallest(matrix, 7))
print(inst.kthSmallest(matrix, 8))
print(inst.kthSmallest(matrix, 9))