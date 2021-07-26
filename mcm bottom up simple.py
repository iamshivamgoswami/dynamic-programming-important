import sys
l=[40, 20, 30, 10, 30]
n=5

dp=[[0]*n for i in range(n)]
for li in range(2,n):
    for i in range(1,n-li+1):
        j=i+li-1
        dp[i][j]=sys.maxsize
        for k in range(i,j):
            temp=dp[i][k]+dp[k+1][j]+l[i-1]*l[k]*l[j]

            dp[i][j]=min(dp[i][j],temp)
print(dp[1][n-1])
print(dp)


