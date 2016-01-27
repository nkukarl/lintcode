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

import math

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        # Write your code here
        nums = sorted(A)
        counter = 0
        for n in A:
            pos = nums.index(n)
            tmp = set(nums[:pos])
            for t in tmp:
                copy = nums[:]
                copy.remove(t)
                counter += self.summarise(copy)
            nums.remove(n)
            
        return counter + 1
        
    def summarise(self, A):
        summary = dict()
        for n in A:
            summary[n] = summary.get(n, 0) + 1
        res = math.factorial(len(A))
        for v in summary.values():
            res //= v
        return res
    

A = [10,10,10,10,9,8,7,6,5,4,3,2,1]

inst = Solution()
print(inst.permutationIndexII(A))