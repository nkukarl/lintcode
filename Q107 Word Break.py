'''
Thoughts:

Since empty string can be broken into words in Dict, initialise array dp with 1 True and n False, n is the length of s

wordBreak_TLE() is trivial,
use i and j to mark the starting (inclusive) and ending (exclusive) of substring of s and check if s[j : i] is in Dict and dp[j] is True, change dp[i] from False to True, exit inner loop

wordBreak() reduces time complexity when s is long, we still need to iterate the index i from the beginning to the end of s, the inner loop iterates all the words in Dict
If word is equal to s[i - len(word) : i] and dp[i - len(word)] is True, dp[i] will then change from False to True, exit the inner loop

Eventually return the last element of dp
'''

class Solution:
    def wordBreak(self, s, Dict):
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for word in Dict:
                if word == s[i - len(word) : i] and dp[i - len(word)]:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak_TLE(self, s, Dict):
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i):
                if s[j : i] in Dict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]

s = 'lintcode'
Dict = ['lint', 'code']

s = 'aaab'
Dict = ['b', 'aa']

inst = Solution()

inst.wordBreak(s, Dict)