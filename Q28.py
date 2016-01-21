class Solution:
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False

		row, col = len(matrix), len(matrix[0])

		if target < matrix[0][-1]:
			r = 0
		if target > matrix[-1][-1]:
			return False

		head, tail = 0, row - 1
		while head < tail:
			mid = (head + tail) // 2
			if matrix[mid][-1] < target:
				head = mid + 1
			else:
				tail = mid
		r = head
		
		if target < matrix[r][0]:
			return False

		head, tail = 0, col - 1
		while head < tail:
			mid = (head + tail) // 2
			if matrix[r][mid] < target:
				head = mid + 1
			else:
				tail = mid

		return matrix[r][head] == target

# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
# target = 24

matrix = [[5]]
target = 2

inst = Solution()
print(inst.searchMatrix(matrix, target))