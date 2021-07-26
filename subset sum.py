class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not sum(nums)%k==0:
            return False

        def subsetSum(nums, summ, n):
            dp = [[False] * (summ + 1) for i in range(n + 1)]

            for i in range(n + 1):
                for j in range(summ + 1):
                    if i == 0:
                        dp[i][j] = False
                    if j == 0:
                        dp[i][j] = True

            for i in range(1, n + 1):
                for j in range(1, summ + 1):
                    if nums[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

                    elif nums[i - 1] > j:
                        dp[i][j] = dp[i - 1][j]
            return dp[-1][-1]
        return subsetSum(nums,sum(nums)//k,len(nums))
