'''
Thoughts:

dfs problem
num2alpha dictionary maps digits to letters
For each level, pick up the first digits and iterate through the letters before entering the next level recursion
When digits reaches None, exit the recursion

'''

num2alpha = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z'), '0': (' ',)}

class Solution:
	def letterCombinations(self, digits):
		self.res = []
		self.helper(digits, '')

		return self.res

	def helper(self, digits, cur):
		if not digits:
			if cur:
				self.res.append(cur)
		else:
			for char in num2alpha[digits[0]]:
				self.helper(digits[1:], cur + char)

digits = '24'

inst = Solution()
print(inst.letterCombinations(digits))
