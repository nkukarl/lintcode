'''
Thoughts:

Create an 'exist' array to store the numbers that are not equal to 1 when doing the repetitive square and sum computation
If a computed number already exists in the 'exist' array, a loop has formed, which means the number is unhappy
Otherwise, return True
helper() does the repetitive computation

'''

class Solution:
	def isHappy(self, n):
		if n == 1:
			return True
		exist = []
		while n != 1:
			n = self.helper(n)
			if n == 1:
				# print(exist)
				return True
			if n in exist:
				# print(exist)
				return False
			exist.append(n)

	def helper(self, n):
		res = 0
		while n:
			res += (n % 10) ** 2
			n //= 10
		return res

n = 3

inst = Solution()
print(inst.isHappy(n))