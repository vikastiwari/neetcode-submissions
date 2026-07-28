class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 1. Setup: Create the dp array. 
        # Every single number is an increasing subsequence of at least length 1!
        dp = [1] * len(nums)
        
        # 2. Main loop: Traverse through every number from left to right
        # We start at index 1 because index 0 has no numbers before it.
        for i in range(1, len(nums)):
            
            # 3. Inner loop: Look backwards at EVERY number that came BEFORE i
            for j in range(0, i):
                
                # If our current number (nums[i]) is STRICTLY greater than the old number (nums[j])
                # it means we can safely attach nums[i] to the end of nums[j]'s sequence!
                if nums[i] > nums[j]:
                    
                    # Update dp[i] to be the maximum of:
                    # 1. Its current value
                    # 2. The length of nums[j]'s sequence PLUS 1 (because we are attaching nums[i])
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        # 4. The longest sequence could have ended anywhere, so we just 
        # return the absolute highest number stored anywhere in the dp array!
        return max(dp)
