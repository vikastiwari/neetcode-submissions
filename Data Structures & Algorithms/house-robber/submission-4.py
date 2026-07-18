class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # The max money if we rob THIS house (n + rob1) vs if we skip this house (rob2)
            temp = max(n + rob1, rob2)
            
            # Shift our variables forward!
            rob1 = rob2
            rob2 = temp
            
        return rob2
