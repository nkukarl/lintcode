class Solution:
	def sortColors2(self, colors):
		pivot = len(colors)
		k = 4
		while k:
			i = 0
			for j in range(pivot):
				if colors[j] != k:
					colors[i], colors[j] = colors[j], colors[i]
					i += 1
			pivot = i
			k -= 1

	def sortColors2_opt(self, colors, k):
		pivot = 0
		n = 1
		while n < k:
			for j in range(pivot, len(colors)):
				if colors[j] == n:
					colors[j], colors[pivot] = colors[pivot], colors[j]
					pivot += 1
			n += 1

import random

colors = [1, 2, 3, 4] * 4
random.shuffle(colors)
print(colors)

inst = Solution()
inst.sortColors2_opt(colors, 4)
print(colors)