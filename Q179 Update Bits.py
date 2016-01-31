class Solution:
    def updateBits_opt(self, m, n, i, j):
        if j < 31:
            mask = ~((1 << (j + 1)) - (1 << i))
        else:
            mask = (1 << i) - 1
        # print(bin(mask))
        res = (mask & m) + (n << i)
        if res > 2 ** 31:
            res -= 2 ** 32
        return res

    def updateBits(self, n, m, i, j):
        if m < 0:
            M = bin((1 << 32) + m)[2:]
        else:
            M = bin(m)[2:]
        if n < 0:
            N = bin((1 << 32) + n)[2:]
        else:
            tmp = bin(n)[2:]
            N = '0' * (32 - len(tmp)) + tmp
        M, N = list(M), list(N)
        N.reverse()
        for k in range(i, j + 1):
            if M:
                tmp = M.pop()
            else:
                tmp = '0'
            N[k] = tmp
        N.reverse()
        N = ''.join(N)
        if N[0] == '1' and len(N) == 32:
            return int(N, 2) - 2 ** 32
        return int(N, 2)


m, n, i, j = 1024, 21, 2, 6
m, n, i, j = 1, -1, 0, 31
m, n, i, j = 456, 31, 27, 31

inst = Solution()
print(inst.updateBits(m, n, i, j))
