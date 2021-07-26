class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp=[[-1]*(n+1) for i in range(W+1)]
        def func(W, weight, values, i=0):
            if dp[W][i]!=-1:
                return dp[W][i]
            if i >= n:
                dp[W][i]=0
                return 0
            if W < 0:
                dp[W][i]=0
                return 0
            if weight[i] > W:
                dp[W][i]=func(W, weight, values, i + 1)
                return func(W, weight, values, i + 1)

            dp[W][i]= max(values[i] + func(W - weight[i], weight, values, i + 1), func(W, weight, values, i + 1))
            return dp[W][i]
        return func(W,wt,val)
# code here
