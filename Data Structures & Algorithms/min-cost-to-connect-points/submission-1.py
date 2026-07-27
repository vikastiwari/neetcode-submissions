class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if points is None:
            return 0

        cost = 0
        visit = set() # 1. Use a set for O(1) lookups
        
        # 2. Just initialize the heap directly!
        min_heap = [(0, 0)]

        while len(visit) < len(points):
            # 3. Remember the heapq. prefix!
            dist, index = heapq.heappop(min_heap) 
            
            if index in visit:
                continue
                
            visit.add(index) # Use .add() for sets
            cost += dist 

            # 4. Don't overwrite the 'points' array! Use range(len())
            for i in range(len(points)):
                if i in visit:
                    continue
                
                # Calculate Manhattan distance
                manhattan = abs(points[index][0] - points[i][0]) + abs(points[index][1] - points[i][1])
                heapq.heappush(min_heap, (manhattan, i))  

        return cost
