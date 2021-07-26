class Solution:
    def lastStoneWeightII(self, arr: List[int]) -> int:

        def subset_sum(arr, n=len(arr), summ=sum(arr)):
            dp = [[False] * (summ + 1) for i in range(n + 1)]
            for i in range(n + 1):
                for j in range(summ + 1):
                    if i == 0:
                        dp[i][j] = False
                    if j == 0:
                        dp[i][j] = True

            for i in range(1, n + 1):
                for j in range(1, summ + 1):
                    if arr[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[n]

        l = subset_sum(arr, n)[:sum(arr) // 2 + 1]

        maxx = 0
        for i in range(len(l)):
            if l[i]:
                maxx = i

        return sum(arr) - 2 * maxx