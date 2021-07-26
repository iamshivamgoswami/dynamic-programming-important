class Solution:
    def isSubsetSum (self, n, arr, target):
        dp = [[False] * (target + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        return dp[-1][-1]