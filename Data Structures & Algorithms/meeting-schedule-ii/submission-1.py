class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. Extract and sort starts and ends independently
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0
        
        # 2. Chronological Sweep
        while s < len(intervals):
            # A meeting started before the earliest one finished
            if starts[s] < ends[e]:
                count += 1
                s += 1
            # A meeting finished!
            else:
                count -= 1
                e += 1
                
            # Keep track of the highest number of concurrent rooms we ever needed
            res = max(res, count)
            
        return res
