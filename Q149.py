class Solution:
	def maxProfit(self, prices):
		if not prices:
			return 0
		P1 = prices[1:]
		P2 = prices[:-1]
		profit = [p1 - p2 for p1, p2 in zip(P1, P2)]
		if max(profit) <= 0:
			return 0
		if min(profit) >= 0:
			return sum(profit)
		cur = 0
		MAX = 0
		for p in profit:
			cur += p
			if cur < 0:
				cur = 0
			else:
				if cur > MAX:
					MAX = cur
		return MAX

prices = [3, 2, 3, 1, 2]

inst = Solution()
print(inst.maxProfit(prices))