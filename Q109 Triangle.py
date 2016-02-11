'''
Thoughts:

Solution_TLE() raises TLE
The best option is to use dynamic programming, initialise dp to be the same size of triangle, but all the elements of dp are 0

For each row of dp, the first and last item of dp shall be obtained by adding the first and last item of the corresponding row in triangle to the first and last item of dp in one row above

For other elements in that row, it shall be formed using the smaller of two adjacent elements in the row above plus the value in corresponding position in triangle

Return the smallest element in the last row of dp

'''

class Solution_opt:
    def minimumTotal(self, triangle):
        m = len(triangle)
        dp = [[0] * i for i in range(1, m + 1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
            
        for i in range(2, m):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        
        return min(dp[-1])

class Solution_TLE:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        left, right = self.split(triangle)
        # print(left, right)
        return triangle[0][0] + min(self.minimumTotal(left), self.minimumTotal(right))

    def split(self, triangle):
        i = 1
        left, right = [], []
        while i < len(triangle):
            left.append(triangle[i][:i])
            right.append(triangle[i][1:])
            i += 1
        return (left, right)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

inst = Solution_TLE()
print(inst.minimumTotal(triangle))

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

inst = Solution_opt()
print(inst.minimumTotal(triangle))