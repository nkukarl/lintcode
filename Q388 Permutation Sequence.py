'''
Thoughts:

factorial array gives the factorial of 0 to n

the k-th permutation is 1 based, minus 1 to convert it into 0 based
Use k divided by factorial of n - 1 to find out which number goes to the first digit, n minus 1 to iterate

'''

class Solution:
	def getPermutation(self, n, k):
		factorial = [1]
		for i in range(1, n + 1):
			factorial.append(factorial[-1] * i)
		k -= 1
		nums = [i for i in range(1, n + 1)]
		res = ''
		while n:
			idx = k // factorial[n - 1]
			res += str(nums.pop(idx))
			k %= factorial[n - 1]
			n -= 1
		return res

n, k = 6, 539
n, k = 3, 1

inst = Solution()
print(inst.getPermutation(n, k))