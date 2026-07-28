class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Default the result to the max number in the array
        # This handles arrays like [-1] correctly
        res = max(nums)
        
        cur_min, cur_max = 1, 1
        
        for n in nums:
            # We must store cur_max temporarily because we overwrite it on the next line,
            # but we still need the old value to calculate cur_min!
            tmp_max = cur_max * n
            
            # The new max is either:
            # 1. The number itself (starting over!)
            # 2. The max so far * n
            # 3. The min so far * n (if both are negative, this becomes a massive positive!)
            cur_max = max(n, cur_max * n, cur_min * n)
            
            # The new min is calculated the exact same way
            cur_min = min(n, tmp_max, cur_min * n)
            
            # Update the global result
            res = max(res, cur_max)
            
        return res
