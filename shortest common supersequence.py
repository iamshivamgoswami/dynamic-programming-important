#User function Template for python3

# User function Template for python3

class Solution:

    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, a, b, m, n):

        n = len(a)
        m = len(b)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m+n-dp[-1][-1]



