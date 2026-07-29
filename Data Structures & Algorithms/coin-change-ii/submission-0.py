class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Create our DP array. 
        dp = [0] * (amount + 1)
        
        # Base Case: There is exactly ONE way to make an amount of 0 (use no coins)
        dp[0] = 1
        
        # CRITICAL: Coins loop MUST be on the outside to prevent duplicate permutations!
        for coin in coins:
            
            # We start the inner loop exactly AT the coin's value
            # (You can't use a 5 cent coin to make an amount of 3 cents)
            for a in range(coin, amount + 1):
                
                # The total ways to make amount 'a' is whatever it already was PLUS
                # the number of ways to make the amount if we subtract this coin
                dp[a] += dp[a - coin]
                
        return dp[amount]
