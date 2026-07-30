class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # 1. Pad the array with 1s on the left and right (as the problem requested)
        # This prevents us from going "out of bounds" when multiplying.
        nums = [1] + nums + [1]
        dp = {}
        
        # 'left' and 'right' define the boundaries of the balloons we are currently popping
        def dfs(left, right):
            # Base Case: There are no balloons left to pop in this range
            if left > right:
                return 0
                
            if (left, right) in dp:
                return dp[(left, right)]
                
            max_coins = 0
            
            # 2. Iterate through every balloon in our current range
            for i in range(left, right + 1):
                
                # Pretend that balloon 'i' is the absolute LAST balloon to pop in this range!
                # If it's the last one, everything else is gone, so it multiplies with the 
                # balloons immediately OUTSIDE our current range (left - 1 and right + 1).
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                
                # Now add the coins we got from popping the left side...
                coins += dfs(left, i - 1)
                
                # ...and add the coins we got from popping the right side!
                coins += dfs(i + 1, right)
                
                # Keep track of whichever balloon gave us the absolute maximum coins
                max_coins = max(max_coins, coins)
                
            dp[(left, right)] = max_coins
            return max_coins

        # We start our DFS from index 1 to len(nums)-2 (because we padded the ends with 1s!)
        return dfs(1, len(nums) - 2)
