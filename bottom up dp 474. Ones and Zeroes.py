import collections


class Solution(object):
    def findMaxForm(self, S, m, n):
        S = [collections.Counter(s) for s in S]

        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, len(S) + 1):
            zero, one = S[i - 1]["0"], S[i - 1]["1"]
            for j in range(n, -1, -1):
                for k in range(m, -1, -1):
                    if k >= zero and j >= one:
                        dp[j][k] = max(dp[j - one][k - zero] + 1, dp[j][k])

                    else:
                        dp[j][k] = dp[j][k]
        return dp[-1][-1]
