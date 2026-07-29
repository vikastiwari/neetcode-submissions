class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2==1:
            return False
        target=target//2
        ary = [False]*(target+1)
        ary[0]=True

        for n in nums:
            for t in range (target,n-1,-1):
                if ary[t-n] :
                    ary[t]=True



        return ary[target]    

        