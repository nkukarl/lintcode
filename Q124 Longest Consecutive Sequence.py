'''
Thoughts:

Use a dictionary summary to record the numbers in nums
Iterate the numbers in nums again, for a certain number n, initialise upper and lower to n + 1 and n - 1
While upper (lower) in summary, delete the corresponding entry in summary and increase (decrease) upper (lower) by 1
Update maxLen when both upper and lower cannot be further extended
The longestConsecutive for n is then upper - lower - 1

FURTHER, this method can also be used to identify integers in an array whose left and right neighbour do not exist in the array
For example, nums = [1, 2, 3, 5, 7, 8, 9, 11, 14]
integers whose left and right neighbour do not exist in nums are: 5, 11, 14, since (4, 6), (10, 12) and (13, 15) do not exist in nums

After running longestConsecutive(), the remaining summary would be {5: 1, 11: 1, 14: 1}, collect the keys of summary would give the target numbers
This is because the entries of those integers who are connected to either neighbour or both neighbours would be deleted
'''

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        summary = dict()
        for n in nums:
            summary[n] = 1

        maxLen = 1
        for n in nums:
            upper = n + 1
            while upper in summary:
                del summary[upper]
                upper += 1
            lower = n - 1
            while lower in summary:
                del summary[lower]
                lower -= 1
            maxLen = max(maxLen, upper - lower - 1)

        return maxLen

nums = [3, 4, 2, 1, 100, 200]

inst = Solution()
print(inst.longestConsecutive(nums))