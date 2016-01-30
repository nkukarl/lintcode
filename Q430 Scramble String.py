'''
Thoughts:

If s1 and s2 are identical, return True
If the length of s1 and s2 are different, return False
Let n represent the length of s1 and s2
If n is 1, return False
If n is 2, check if s1 is the inverse of s2
Otherwise, for i from 1 to n - 1 (inclusive), split s1 and s2 into two different sets of pairs of two
s1[:i], s2[:i] and s1[i:], s2[i:] (left vs left, right vs right)
or
s1[:i], s2[:-i] and s1[i:], s2[-i:] (left vs right, right vs left)
Recursively check isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]),
or isScramble(s1[:i], s2[:-i]) and isScramble(s1[i:], s2[-i:])
Return True if either one returns True
Otherwise, return False outside the loop

FURTHER, for long s1 and s2, it might require a dictionary to store those pairs that have been checked to reduce time complexity


'''

class Solution:
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if n == 1:
            return False
        if n == 2:
            return s1 == s2[::-1]
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False

s1 = 'great'
s2 = 'rgeat'
s2 = 'rgtae'

inst = Solution()
print(inst.isScramble(s1, s2))