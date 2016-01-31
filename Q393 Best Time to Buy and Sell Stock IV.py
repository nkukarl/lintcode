'''
Thoughts:

Let m denote the length of prices
Initialise dp to k + 1 rows of [0] * m
Iterate row from 1 to k + 1 and col from 1 to m
There is no need to deal with the first row of dp there is not transaction and there is also no need to deal with the first column of dp since there is only one prices, and no transaction could happen

Take k, prices = 3, [1, 4, 2, 7, 5, 8] as an example
   1  4  2  7  5  8
0 [0, 0, 0, 0, 0, 0]
1 [0, 3, 3, 6, 6, 7]
2 [0, 3, 3, 8, 8, 9]
3 [0, 3, 3, 8, 8, 11]

To obtain the profit for dp[row][col], one can either do no transaction for prices[col], thus the profit is dp[row][col - 1]
Otherwise, buy the stock at prices[c] and sell it at prices[col], the total profit would be dp[row - 1][c] plus prices[col] - prices[c]
c could iterate between 0 (inclusive) to col (exclusive)

Eventually, dp[-1][-1] shall be returned

However, this leads to TLE since O(k * m * m) time is needed

To get rid of duplicated calculations, we can look at the equation
dp[row - 1][c] + prices[col] - prices[c]
Rearrange it into prices[col] + dp[row - 1][c] - prices[c]
This translates into finding out the maximum between dp[row - 1][c] and prices[c]
Let cur = dp[row - 1][0] - prices[0]

When iterating col from 1 (inclusive) to m (exclusive), compare dp[row - 1][col - 1] - price[col - 1] to cur and update cur to the larger one
Hence, dp[row][col] shall arise from cur + prices[col] and dp[row][col - 1]

This reduces time complexity to O(k * m)

However, this still lead to MLE when k is large

As a result, let dp = [0] * m and initialise tmp to [0] at the beginning of each iteration of row, append the maximum profit found to tmp for each iteration of col, and update dp to tmp at the end of each iteration of row

Return dp[-1]

A corner case is when k > m // 2 (the number of transactions allowed is greater than half of the size of prices), the problem is then convert to Best Time to Buy and Sell Stock IV since one can complete as many transactions as you want

'''

class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        m = len(prices)

        '''
        Corner case
        '''
        if k > m // 2:
            ans = 0
            tmp = [a - b for a, b in zip(prices[1:], prices[:-1])]
            for t in tmp:
                if t > 0:
                    ans += t
            return ans

        dp = [0] * m

        for row in range(1, k + 1):
            cur = dp[0] - prices[0]
            tmp = [0]
            for col in range(1, m):
                cur = max(cur, dp[col - 1] - prices[col - 1])
                tmp.append(max(cur + prices[col], tmp[-1]))

            dp = tmp[:]

        return dp[-1]

    def maxProfit_MLE(self, k, prices):
        if not prices:
            return 0
        m = len(prices)

        # See explanation for this segment in maxProfit()
        if k > m // 2:
            ans = 0
            tmp = [a - b for a, b in zip(prices[1:], prices[:-1])]
            for t in tmp:
                if t > 0:
                    ans += t
            return ans

        dp = [[0] * m for _ in range(k + 1)]
        for row in range(1, k + 1):
            cur = dp[row - 1][0] - prices[0]
            for col in range(1, m):
                cur = max(cur, dp[row - 1][col] - prices[col])
                dp[row][col] = max(cur + prices[col], dp[row][col - 1])
                

        for line in dp:
            print(line)

        return dp[-1][-1]


    def maxProfit_TLE(self, k, prices):
        if not prices:
            return 0
        m = len(prices)
        dp = [[0] * m for _ in range(k + 1)]
        for row in range(1, k + 1):
            for col in range(1, m):
                tmp = 0
                for c in range(col):
                    tmp = max(tmp, dp[row - 1][c] + prices[col] - prices[c])
                dp[row][col] = max(dp[row][col - 1], tmp)

        return dp[-1][-1]


k, prices = 3, [1, 4, 2, 7, 5, 8]
k, prices = 3, [4, 4, 6, 1, 1, 4, 2, 5]


inst = Solution()
print(inst.maxProfit(k, prices))