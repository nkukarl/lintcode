'''
Thoughts:

The implementation of backPack_MLE() is easier to understand, and backPack() simply optimise the memory to avoid MLE

Sort A in ascending order first

Using dynamic programming, let n = len(A) and initialise dp to
[[0] * (m + 1) for _ in range(n + 1)]
dp[i][j] then represents the whether a backpack with size j can be filled using the first i items in A (first i items means items A[0] to A[i - 1])

Since a backpack with size 0 can always be filled, the first column of dp shall be 1
Alternatively, dp can be directly initialised to
[[1] + [0] * m for _ in range(n + 1)]

Iterate the rows and columns of dp using iterator i and j, respectively
i ranges from 1 to n (inclusive), and j ranges from 1 to m (inclusive)

For dp[i][j], if j < A[i - 1], element A[i - 1] has not been used to fill the backpack, thus dp[i][j] will simply copy the value of dp[i - 1][j]
Otherwise, j >= A[i - 1], element A[i - 1] is now being used to fill the backpack,
Same as the j < A[i - 1] scenario, if dp[i - 1][j] is 1, dp[i][j] is 1
In addition, if dp[i - 1][j - A[i - 1]] is 1, then dp[i][j] is 1

In order to obtain the maximum size that the backpack can be filled, the bottom row of dp is then taken into consideration
The index of the first 1 from the right of the bottom row of dp then corresponds to the maximum size
In terms of implementation, let tmp equal the bottom row of dp
While the last element of tmp is 0, it is popped out
Return the length of tmp minus 1

Since the value of dp[i][j] is only related to the values in the above row, an array instead of a matrix can be used for dp
The optimised solution initialises dp to [1] + [0] * m
The iterations are the same, yet in the outer loop, a tmp array is initialised to [1] and the calculated value is appended to tmp for each inner loop
dp is then updated to tmp at the end of each outer loop iteration
To find out the maximum size, dp is then processed using the implementation mentioned above

'''

class Solution:
    def backPack(self, m, A):

        A.sort()

        n = len(A)
        
        dp = [1] + [0] * m
        
        for i in range(1, n + 1):
            tmp = [1]
            for j in range(1, m + 1):
                if j < A[i - 1]:
                    tmp.append(dp[j])
                else:
                    tmp.append(dp[j] or dp[j - A[i - 1]])
            dp = tmp[:]
            
        while dp:
            if dp[-1] == 0:
                dp.pop()
            else:
                return len(dp) - 1
    
    def backPack_MLE(self, m, A):
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j < A[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]

        tmp = dp[-1]
        while tmp:
            if tmp[-1] != 1:
                tmp.pop()
            else:
                return len(tmp) - 1

m = 11
A = [2, 3, 5, 7]

m = 10
A = [3, 4, 5, 8]

inst = Solution()
print(inst.backPack(m, A))