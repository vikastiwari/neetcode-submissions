class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        ans=0
        
        if len(nums)==1:
            return nums[0]
        
            

        for index,n in enumerate(nums):
            if index==len(nums)-1:
                continue
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp
            
        ans = rob2
        rob1, rob2 = 0, 0 
        for index,n in enumerate(nums):
            if index==0:
                continue
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp
            
        return max (ans, rob2)

