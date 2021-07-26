class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False

        dp = [[False] * (sum(nums) // 2 + 1) for i in range(n + 1)]

        def subset_sum(nums, n, summ=sum(nums) // 2):
            for i in range(n + 1):
                for j in range(summ + 1):
                    if j == 0:
                        dp[i][j] = True

            for i in range(1, n + 1):
                for j in range(1, summ + 1):
                    if nums[i - 1] > j:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

            return dp[-1][-1]

        return subset_sum(nums, len(nums))

