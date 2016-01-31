'''
Thoughts:

Take word1 == 'abcdef' and word2 = 'azced' as an example, m and n are the length of word1 and word2, respectively
m = 6, n = 5
Initialise dp to m + 1 rows of [0] * (n + 1), update the elements in the first row and the first column to their corresponding column and row number, and dp looks like
[0, 1, 2, 3, 4, 5]
[1, 0, 0, 0, 0, 0]
[2, 0, 0, 0, 0, 0]
[3, 0, 0, 0, 0, 0]
[4, 0, 0, 0, 0, 0]
[5, 0, 0, 0, 0, 0]
[6, 0, 0, 0, 0, 0]

Let dp[i][j] represents the number of edits required to convert the first i letters of word1 into the first j letters of word2
Iterate word1 and word2 using i and j respectively
If word1[i] == word2[j], 0 edit is required, dp[i][j] = dp[i - 1][j - 1]
Otherwise, one more edit is required and hence shall arise from 1 plus the smallest of dp[i - 1][j - 1], dp[i][j - 1] and dp[i - 1][j]
dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

Return dp[-1][-1]

'''

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for col in range(n + 1):
            dp[0][col] = col

        for row in range(m + 1):
            dp[row][0] = row

        # for line in dp:
        #     print(line)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        # for line in dp:
        #     print(line)

        return dp[-1][-1]


word1 = 'abcdef'
word2 = 'azced'

inst = Solution()
inst.minDistance(word1, word2)