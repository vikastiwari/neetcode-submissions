class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer=nums[0]
        our_sum=0
        for num in nums:
            if our_sum<0:
                our_sum=0
            our_sum+=num
            answer = max(answer,our_sum)  
        return answer      
        