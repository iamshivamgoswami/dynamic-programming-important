import math


class Solution:

    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        target = n
        arr = [x, y, z]

        n = len(arr)
        dp = [[-math.inf] * (target + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if j == 0:
                    dp[i][j] = 0

        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - arr[i - 1]] + 1)

        return dp[n][target] if dp[n][target] != -math.inf else 0