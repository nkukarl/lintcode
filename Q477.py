class Solution:
	def surroundedRegions(self, board):
		if board:
			self.row, self.col = len(board), len(board[0])
			for c in range(self.col):
				if board[0][c] == 'O':
					self.helper(board, 0, c)
				if board[self.row - 1][c] == 'O':
					self.helper(board, self.row - 1, c)
			for r in range(self.row):
				if board[r][0] == 'O':
					self.helper(board, r, 0)
				if board[r][self.col - 1] == 'O':
					self.helper(board, r, self.col - 1)
			for r in range(self.row):
				for c in range(self.col):
					if board[r][c] == 'O':
						board[r][c] = 'X'
			for r in range(self.row):
				for c in range(self.col):
					if board[r][c] == '$':
						board[r][c] = 'O'

	def helper(self, board, r, c):
		if r < 0 or c < 0 or r > self.row - 1 or c > self.col - 1 or board[r][c] != 'O':
			return
		board[r][c] = '$'
		self.helper(board, r - 1, c)
		self.helper(board, r + 1, c)
		self.helper(board, r, c - 1)
		self.helper(board, r, c + 1)

board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'X', 'X', 'X']]

inst = Solution()
inst.surroundedRegions(board)