class Solution:
    def aplusb(self, a, b):
        mask = 2 ** 32
        while b != 0:
            if b == mask:
                return a ^ -mask
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

a, b = -13, 1

inst = Solution()
print(inst.aplusb(a, b))