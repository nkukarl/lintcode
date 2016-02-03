'''
Thoughts:

Denote the length of ratings as n
Initialise candies to [1] * n

Iterate ratings from 1 to n - 1, if ratings[i] > ratings[i - 1], let candies[i] be candies[i - 1] + 1
Iterate ratings in the reverse order, from n - 2 to 0, if ratings[i] > ratings[i + 1], let candies[i] be the larger value of candies[i] and candies[i + 1] + 1

'''

class Solution:
	def candy(self, ratings):
		n = len(ratings)
		candies = [1] * n

		for i in range(1, n):
			if ratings[i] > ratings[i - 1]:
				candies[i] += 1
		for i in range(n - 2, -1, -1):
			if ratings[i] > ratings[i + 1]:
				candies[i] = max(candies[i], candies[i + 1] + 1)

		return sum(candies)

ratings = [1, 2]
# ratings = [1, 1, 1]
# ratings = [1, 2, 2]

inst = Solution()
print(inst.candy(ratings))