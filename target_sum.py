class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        target,m=divmod((sum(nums)+target),2)
        if m:
            return 0

        def subset_sum(nums,target,n=len(nums)):
            dp=[[0]*(target+1)for i in range(n+1)]
            for i in range(n+1):
                dp[i][0]=1
            for i in range(1,n+1):
                for j in range(1,target+1):
                    if nums[i-1]>j:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j]

            return dp[-1][-1]
        return subset_sum(nums,target)
