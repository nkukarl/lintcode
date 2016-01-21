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