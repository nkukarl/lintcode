'''
Thoughts:

Let n = a_x * 5 ** x + a_x-1 * 5 ** x - 1 + ... + a_1 * 5 ** 1 + a_0 * 5 ** 0
Find the smallest x that would be make 5 ** x larger than or equal to n
Put a_x to a_1 in tmp array
Calculate the number of 5s for each 5 ** x, put them in count
A simple relation is count[0] = 1, count[n] = count[n - 1] * 5 + 1
Multiply tmp by count in element wise, the sum of the multiplication would be the answer


'''

class Solution:
	def trailingZeros(self, n):
		exp = 0
		while 5 ** exp <= n:
			exp += 1
		exp -= 1
		count = self.helper(exp)
		# print('count:', count)
		tmp = []
		while exp:
			tmp.append(n // 5 ** exp)
			n %= 5 ** exp
			exp -= 1
		tmp.reverse()
		# print(tmp)
		res = sum([a * b for a, b in zip(count, tmp)])

		return res
		
	def helper(self, n):
		res = [1]
		for i in range(n - 1):
			res.append(res[-1] * 5 + 1)
			
		return res

inst = Solution()
print(inst.trailingZeros(20))

print(inst.helper(4))