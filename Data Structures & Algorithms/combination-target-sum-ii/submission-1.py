class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        subSet=[]
        candidates.sort()

        def dfs(index,sum):
            if sum==target:
                ans.append(subSet.copy())
                return
            if sum>target or index>=len(candidates):
                return

            subSet.append(candidates[index])
            dfs(index+1,sum+candidates[index])

            pop = subSet.pop()

            while index+1 < len(candidates) and candidates[index]==candidates[index+1] :
                index+=1

            dfs(index+1,sum)        

        dfs(0,0)
        return ans    

        