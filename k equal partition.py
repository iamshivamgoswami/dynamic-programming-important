class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        n=len(nums)
        if k>n:
            return False
        if sum(nums)%k!=0:
            return False
        if k==1:
            return True

        visited=[False]*n
        summ=sum(nums)

        def dfs(nums, summ, st, visited, target, round):

            if round == 0:
                return True
            if summ == target and dfs(nums, 0, len(nums) - 1, visited, target, round - 1):
                return True
            for i in range(st, -1, -1):
                if not visited[i] and summ + nums[i] <= target:
                    visited[i] = True
                    if dfs(nums, summ + nums[i], i - 1, visited, target, round):
                        return True
                    visited[i] = False

            return False

        return dfs(nums, 0, len(nums) - 1, visited, summ / k, k)
