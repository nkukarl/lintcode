'''
Thoughts:

Initialise nums to be sorted A and initialise counter to 0
For each n in A, locate n in nums
All the unique elements in nums that are less than n make a tmp array
For each element t in tmp, let copy equals to nums
Remove t from copy and summarise the occurrence of each element in copy
The total permutation of elements in copy can then be calculated and added to counter
Remember to add 1 to counter at the end since it is 1 based rather than 0 based counting

'''


class Solution:
	def permutationIndexII(self, A):
		nums = sorted(A)
		counter = 0
		for n in A:
			tmp = nums[:nums.index(n)]
			tmp = list(set(tmp))
			for t in tmp:
				copy = nums[:]
				copy.remove(t)
				counter += self.perm(copy)
			nums.remove(n)
		return counter + 1

	def perm(self, A):
		summary = dict()
		for n in A:
			summary[n] = summary.get(n, 0) + 1
		res = self.factorial(len(A))
		for val in summary.values():
			res //= self.factorial(val)
		return res

	def factorial(self, n):
		if n <= 1:
			return 1
		res = 1
		i = 2
		while i <= n:
			res *= i
			i += 1
		return res

A = [4, 2, 1, 2]
A = [10,10,10,10,9,8,7,6,5,4,3,2,1]

inst = Solution()
print(inst.permutationIndexII(A))