import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by start time
        intervals.sort()
        
        # 2. We need to answer queries in increasing order, but we MUST remember 
        # their original indices so we can put the answers in the correct spot!
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        res = [-1] * len(queries)
        minHeap = []
        i = 0
        
        # 3. Process each query from smallest to largest
        for q, original_index in sorted_queries:
            
            # Step A: Push ALL intervals that start BEFORE or AT this query into the heap.
            # We push the (length, end_time) because we want the shortest length!
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(minHeap, (length, right))
                i += 1
                
            # Step B: Remove intervals from the heap that have already ended!
            # If the end time is less than our current query 'q', it's expired.
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            # Step C: The top of the heap is GUARANTEED to be the shortest valid interval!
            if minHeap:
                res[original_index] = minHeap[0][0]
                
        return res
