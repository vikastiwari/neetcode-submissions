class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. The Golden Rule: Sort by start time!
        intervals.sort(key=lambda i: i[0])
        
        # 2. Seed our result with the first interval
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            
            # The end time of the LAST interval we placed in our result
            last_end = res[-1][1]
            
            # Case 1: Overlap! (Absorb it by stretching the end time)
            if current_start <= last_end:
                res[-1][1] = max(last_end, current_end)
                
            # Case 2: No Overlap! (Add it as a new block)
            else:
                res.append(intervals[i])
                
        return res
