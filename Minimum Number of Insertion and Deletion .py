def func(a,b):
    n=len(a)
    m=len(b)
    dp=[[0]*(m+1)for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[-1][-1])
    return dp[-1][-1]

a="heap"
b="pea"
print(len(a)+len(b)-2*func(a,b))