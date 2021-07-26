class Solution:
    def LongestRepeatingSubsequence(self, a):

    b = a
    n = len(a)

    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1] and i != j:

                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
