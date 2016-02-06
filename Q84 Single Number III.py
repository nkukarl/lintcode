'''
Thoughts:

If there are two different single numbers (denoted as a and b), they differ at least one bit in binary forms
Hence, firstly find a ^ b by using the same iteration in Q82 Single Number
Find the lowest non-zero bit of a ^ b, define it as mask

Items in A can then be divided into two groups, those xor mask give 0 and those xor mask do not give 0
a, b are separated into these two groups and all the elements in each of these two groups have two occurrences
Let a, b = 0, 0, for the first group, xor each of them with a and for the second group, xor each of them with b

Return a, b

'''

class Solution:
    def singleNumberIII(self, A):
        tmp = 0
        for n in A:
            tmp ^= n
        
        mask = 1
        while tmp:
            if tmp & 1:
                break
            mask <<= 1
            tmp >>= 1
        
        a, b = 0, 0
        for n in A:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        
        return a, b

class Solution_extra_memory:
    def singleNumberIII(self, A):
        tmp = self.singleNumber(A)

        mask = 1
        while tmp:
            if tmp & 1 == 0:
                tmp >>= 1
                mask <<= 1
            else:
                break

        A1, A2 = [], []
        for n in A:
            if n & mask == 0:
                A1.append(n)
            else:
                A2.append(n)
        print(A1, A2)

        a, b = self.singleNumber(A1), self.singleNumber(A2)

        return [a, b]

    def singleNumber(self, A):
        if not A:
            return 0
        tmp = 0
        for n in A:
            tmp ^= n
        return tmp


A = [1, 2, 2, 3, 4, 4, 9, 3]
A = [4, 12]

inst = Solution()
print(inst.singleNumberIII(A))