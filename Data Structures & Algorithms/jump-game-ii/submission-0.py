class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = 0
        right = 0
        
        # We loop until our 'right' boundary covers the end of the array
        while right < len(nums) - 1:
            farthest = 0
            
            # Scan everything in our current window to find the absolute farthest jump
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
                
            # We finished scanning the window. That means we have to take a jump!
            # Shift the window forward.
            left = right + 1
            right = farthest
            jumps += 1
            
        return jumps
