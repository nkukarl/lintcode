class Solution:
	def isValidSudoku(self, board):
		# check size
		m, n = len(board), len(board[0])
		if m != 9 or n != 9:
			return False

		# check row
		for row in range(m):
			tmp = []
			for col in range(n):
				if board[row][col] != '.':
					tmp += [board[row][col]]
			# print(tmp)
			if len(set(tmp)) != len(tmp):
				return False

		# check col
		for col in range(n):
			tmp = []
			for row in range(m):
				if board[row][col] != '.':
					tmp += [board[row][col]]
			# print(tmp)
			if len(set(tmp)) != len(tmp):
				return False

		# check block
		pivot = [0, 3, 6]
		for top in pivot:
			bottom = top + 3
			for left in pivot:
				right = left + 3
				tmp = []
				for row in range(top, bottom):
					for col in range(left, right):
						if board[row][col] != '.':
							tmp += [board[row][col]]
				# print(tmp)
				if len(set(tmp)) != len(tmp):
					return False

		return True

board = [
".87954321",
"2....7...",
"3.1...5..",
"4.3.6....",
"5...2....",
"6.2.4....",
"7.6....9.",
"8.5....1.",
"9......4."
]


inst = Solution()
print(inst.isValidSudoku(board))
