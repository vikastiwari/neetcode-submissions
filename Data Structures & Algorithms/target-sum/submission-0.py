class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i,our_sum):
            if i==len(nums):
                if our_sum==target:
                    return 1
                else:
                    return 0

            return dfs(i+1,our_sum+nums[i]) + dfs(i+1,our_sum-nums[i])    

        
        return dfs(0,0)