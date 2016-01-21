class Solution:
	def maxProfit(self, prices):
		P1 = prices[1:]
		P2 = prices[:-1]
		profits = [p1 - p2 for p1, p2 in zip(P1, P2)]
		profit = 0
		for p in profits:
			if p > 0:
				profit += p
		return profit