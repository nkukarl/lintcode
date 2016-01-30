'''
Thoughts:

Similar to Maximum Subarray II

The difference is that we never do negative profit, hence, the subarray could contain 0 or more elements, which is unlike the Maximum Subarray II problem where the subarray shall have 1 or more elements
Another difference is that the numbers are prices, instead of profits, hence we shall convert prices into profits using elementwise subtract between prices[1:] and [:-1]
N.B. If len(prices) <= 1, simply return 0 since no transaction can be done

Simply apply helper() twice to get the ongoing maximum from left to right and right to left
In helper(), let cur be the larger one of 0 and profits[0], initialise res to [cur]
Iterate all the profits in profits[1:], let cur be updated to the larger one of the original cur and 0 and let the ongoing maximum be updated to the larger one of the original maximum and cur
Return res at the end of helper()

Instead of popping out the last element of l2r and the first element of r2l, we insert 0 to the beginning of l2r and append 0 to the end of r2l
Use res to record the elementwise addition of l2r and r2l, return the max

'''

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        # write your code here
        profits = [a - b for a, b in zip(prices[1:], prices[:-1])]
        l2r = self.helper(profits)
        r2l = self.helper(profits[::-1])[::-1]
        
        l2r.insert(0, 0)
        r2l.append(0)
        
        res = [a + b for a, b in zip(l2r, r2l)]
        
        return max(res)
        
    def helper(self, profits):
        cur = max(profits[0], 0)
        res = [cur]
        for p in profits[1:]:
            cur += p
            # if cur < 0:
            #     cur = 0
            #     res.append(res[-1])
            # else:
            #     res.append(max(cur, res[-1]))

            # more concise
            cur = max(0, cur)
            res.append(max(cur, res[-1]))
                
        return res

prices = [2, 1, 2, 0, 1]

inst = Solution()
print(inst.maxProfit(prices))