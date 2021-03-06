'''
Thoughts:

Iterate all the characters in board, if board[r][c] equal to word[0:], enter helper function with r, c and word[1:]
When r or c exceeds the edges, exit helper function
If the first letter of current word can be found by extending position [r][c] in any direction, enter helper function with updated r, c and word
Valid array is used to record whether a certain character has been used already when searching for the word


'''

class Solution:
	def exist(self, board, word):
		if not word:
			return True
		if not board:
			return False
		row, col = len(board), len(board[0])
		self.row, self.col = row, col
		valid = [[0] * col for _ in range(row)]
		for r in range(row):
			for c in range(col):
				if board[r][c] == word[0]:
					tmp = valid[:r] + [valid[r][:c] + [1] + valid[r][c + 1:]] + valid[r + 1:]
					# print(tmp)
					if self.helper(board, word[1:], tmp, r, c):
						return True
		return False

	def helper(self, board, word, valid, r, c):
		if not word:
			return True
		if r < 0 or c < 0 or r >= self.row or c >= self.col:
			return False
		if r > 0:
			if board[r - 1][c] == word[0] and valid[r - 1][c] != 1:
				tmp = valid[:r - 1] + [valid[r - 1][:c] + [1] + valid[r - 1][c + 1:]] + valid[r:]
				if self.helper(board, word[1:], tmp, r - 1, c):
					return True
		if r < self.row - 1:
			if board[r + 1][c] == word[0] and valid[r + 1][c] != 1:
				tmp = valid[:r + 1] + [valid[r + 1][:c] + [1] + valid[r + 1][c + 1:]] + valid[r + 2:]
				if self.helper(board, word[1:], tmp, r + 1, c):
					return True
		if c > 0:
			if board[r][c - 1] == word[0] and valid[r][c - 1] != 1:
				tmp = valid[:r] + [valid[r][:c - 1] + [1] + valid[r][c:]] + valid[r + 1:]
				if self.helper(board, word[1:], tmp, r, c - 1):
					return True
		if c < self.col - 1:
			if board[r][c + 1] == word[0] and valid[r][c + 1] != 1:
				tmp = valid[:r] + [valid[r][:c + 1] + [1] + valid[r][c + 2:]] + valid[r + 1:]
				if self.helper(board, word[1:], tmp, r, c + 1):
					return True
		return False


board = ['ABCE', 'SFCS', 'ADEE']
words = ['ABCCED', 'SFCS', 'EEDA', 'ABCB']
inst = Solution()
for word in words:
	print(word, inst.exist(board, word))