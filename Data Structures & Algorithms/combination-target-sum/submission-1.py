class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        subSet=[]

        def dfs(index,sum) :
            if sum==target:
                ans.append(subSet.copy())
                return

            if sum>target or index>=len(nums):
                return

            subSet.append(nums[index])
            dfs(index,sum+nums[index])

            subSet.remove(nums[index])
            dfs(index+1,sum)


        dfs(0,0)
        return ans            
