class Solution:
	def majorityNumber(self, nums):
		if not nums:
			return None
		a, b = None, None
		countA, countB = 0, 0

		for n in nums:
			if not a and not b:
				a = n
				countA = 1
			elif not b:
				if n == a:
					countA += 1
				else:
					b = n
					countB = 1
			elif not a:
				if n == b:
					countB += 1
				else:
					a = n
					countA = 1
			else:
				if n == a:
					countA += 1
				elif n == b:
					countB += 1
				else:
					countA -= 1
					countB -= 1
					if countA == 0:
						a = None
						countA = 0
					if countB == 0:
						b = None
						countB = 0

		countA, countB = 0, 0
		for n in nums:
			if n == a:
				countA += 1
			elif n == b:
				countB += 1
		if countA > countB:
			return a
		return b

nums = [1, 2, 1, 2, 1, 3, 3, 3, 3]

inst = Solution()
print(inst.majorityNumber(nums))