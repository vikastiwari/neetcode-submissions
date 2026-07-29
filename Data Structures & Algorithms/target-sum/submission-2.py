class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,our_sum):
            if i==len(nums):
                if our_sum==target:
                    return 1
                else:
                    return 0
            if (i,our_sum) in dp:
                return dp[(i,our_sum)]
            dp[(i,our_sum)] = dfs(i+1,our_sum+nums[i]) + dfs(i+1,our_sum-nums[i])
            return  dp[(i,our_sum)]   
        return dfs(0,0)