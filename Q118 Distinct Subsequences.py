'''
Thoughts:

Two solutions use the same dynamic programming method, the second one optimises the memory, reducing it from O(mn) to O(n)

Let m and n denote the length of s and t
Initialise dp to m + 1 rows of [1] + [0] * n,
which looks like
[
[1, 0, 0, ..., 0],
[1, 0, 0, ..., 0],
...,
[1, 0, 0, ..., 0]
]

Iterate s and t using iterator r and c respectively,
Let dp[r][c] represents in the first r letters of s and c letters of t, how many distinct subsequences there are.
If s[r - 1] == t[c - 1], dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]
Otherwise, dp[r][c] = dp[r - 1][c]
Return dp[-1][-1]

numDistinct_opt() reduces memory use by replacing dp as [1] + [0] * n
When iterating r, let tmp be initialised to [1] and append elements to tmp when iterating c
Update dp to tmp at the end of each iteration of r
Return dp[-1]

'''

class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[1] + [0] * n for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if s[r - 1] == t[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c]

        return dp[-1][-1]

    def numDistinct_opt(self, s, t):
        m, n = len(s), len(t)
        dp = [1] + [0] * n

        for r in range(1, m + 1):
            tmp = [1]
            for c in range(1, n + 1):
                if s[r - 1] == t[c - 1]:
                    tmp.append(dp[c - 1] + dp[c])
                else:
                    tmp.append(dp[c])
            dp[:] = tmp[:]
        return dp[-1]
    

s = 'rabbbit'
t = 'rabbit'

s = 'aacecscesec'
t = 'ces'

inst = Solution()
print(inst.numDistinct(s, t))