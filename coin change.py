class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[math.inf] * (amount + 1) for i in range(len(coins) + 1)]

        n = len(coins)
        for i in range(1, n + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])

        return dp[n][amount] if dp[n][amount] != math.inf else -1