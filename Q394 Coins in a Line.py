'''
Thoughts:

Trivial

If n is a multiple of 3:
If the first player takes X, then the second play always takes 3 - X, the first player would lose
If n is not a multiple of 3:
The first player would take X to make the remaining n a multiple of 3, hence the first player can win

'''

class Solution:
	def firstWillWin(self, n):
		if n % 3 == 0:
			return False
		return True