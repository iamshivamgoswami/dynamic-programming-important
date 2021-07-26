class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = n
        j = m
        ans = ""
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                ans += a[i - 1]
                i -= 1
                j -= 1

            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    ans+=a[i-1]
                    i -= 1
                else:
                    ans+=b[j-1]
                    j -= 1

        while i>0:
            ans+=a[i-1]
            i-=1
        while j>0:
            ans+=b[j-1]
            j-=1
        return ans[::-1]

