class Solution:
    def matrixMultiplication(self, n, arr):

        dp = [[float("inf")] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for l in range(2, n):
            for i in range(1, n - l + 1):
                j = i + l - 1

                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                    dp[i][j] = min(cost, dp[i][j])

        return dp[1][n - 1]

