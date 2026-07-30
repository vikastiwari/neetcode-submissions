class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Place the goal post at the final index
        goal = len(nums) - 1
        
        # 2. Walk backwards through the array (starting from second to last)
        for i in range(len(nums) - 2, -1, -1):
            
            # The Greedy Choice: Can we reach the goal from our current position?
            if i + nums[i] >= goal:
                # If yes, shift the goal post to our current position!
                goal = i
                
        # 3. If the goal post made it all the way back to the start, we win.
        return goal == 0
