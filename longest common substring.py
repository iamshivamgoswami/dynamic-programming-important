class Solution:
    def longestCommonSubstr(self, a, b, n, m):
        # code here
        dp=[[0]*(m+1)for i in range(n+1)]
        maxx=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    maxx=max(maxx,dp[i][j])
                else:
                    dp[i][j]=0
        return maxx