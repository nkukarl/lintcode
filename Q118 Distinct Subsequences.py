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

'''


        r   a   b   b   i   t
    1   0   0   0   0   0   0
r   1   1   0   0   0   0   0
a   1   1   1   0   0   0   0
b   1   1   1   1   0   0   0
b   1   1   1   2   1   0   0
b   1   1   1   3   3   0   0
i   1   1   1   3   3   3   0
t   1   1   1   3   3   3   3
'''

s = 'aacecscesec'
t = 'aces'

'''
        a   c   e   s
    1   0   0   0   0
a   1   1   0   0   0
a   1   2   0   0   0
c   1   2   2   0   0
e   1   2   2   2   0
c   1   2   4   2   0
s   1   2   4   2   2
c   1   2   6   2   2
e   1   2   6   8   2
s   1   2   6   8   10
e   1   2   6   14  10
c   1   2   8   14  10

'''

inst = Solution()
print(inst.numDistinct(s, t))