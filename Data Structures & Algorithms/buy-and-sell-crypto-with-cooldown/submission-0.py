class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        # 'i' is the day.
        # 'buying' is True if we are looking to buy. It's False if we own a stock and need to sell.
        def dfs(i, buying):
            # Base Case: We ran out of days. We can't make any more money.
            if i >= len(prices):
                return 0
                
            if (i, buying) in dp:
                return dp[(i, buying)]
                
            # STATE 1: We are looking to BUY
            if buying:
                # Choice 1: Buy today! 
                # We LOSE money today, move to day i+1, and switch to "selling" mode (not buying)
                buy = dfs(i + 1, not buying) - prices[i]
                
                # Choice 2: Cooldown (Skip)
                # We lose 0 money, move to day i+1, and stay in "buying" mode
                cooldown = dfs(i + 1, buying)
                
                # Cache the best choice
                dp[(i, buying)] = max(buy, cooldown)
                
            # STATE 2: We own a stock and are looking to SELL
            else:
                # Choice 1: Sell today!
                # We GAIN money today, switch to "buying" mode, but we MUST SKIP tomorrow (i+2) because of cooldown!
                sell = dfs(i + 2, not buying) + prices[i]
                
                # Choice 2: Cooldown (Hold)
                # We gain 0 money, move to day i+1, and stay in "selling" mode
                cooldown = dfs(i + 1, buying)
                
                # Cache the best choice
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
            
        # Start on day 0, and we are allowed to buy!
        return dfs(0, True)
