class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[None] * (W + 1) for i in range(N + 1)]

        def func(N, W, val, wt):
            for i in range(0, N + 1):
                for j in range(0, W + 1):
                    dp[i][j] = 0
            for i in range(1, N + 1):
                for j in range(1, W + 1):
                    if wt[i - 1] <= j:
                        dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j])
                    else:

                        dp[i][j] = dp[i - 1][j]

            return dp[N][W]

        return func(N, W, val, wt)
val=[1,1,1]
W=7
N=3
wt=[5,5,2]
a=Solution()
print(a.knapSack(N,W,val,wt))
