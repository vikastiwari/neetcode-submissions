class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Start at the 3rd to last step, and walk backwards to index 0!
        # The loop goes from len(cost)-3 down to 0
        for i in range(len(cost) - 3, -1, -1):
            
            # The cheapest way to climb from this current step is its own cost, 
            # PLUS the minimum of the two steps directly in front of it!
            # TODO: cost[i] += min(???, ???)
            cost[i] += min(cost[i+1],cost[i+2])
            
            
        # We are allowed to start at index 0 or index 1. Return the cheapest one!
        return min(cost[0], cost[1])
