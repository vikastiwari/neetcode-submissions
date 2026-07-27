class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if points is None:
            return 0

        cost = 0
        visit = set() 
        
        min_heap = [(0, 0)]

        while len(visit) < len(points):
            dist, index = heapq.heappop(min_heap) 
            
            if index in visit:
                continue
                
            visit.add(index) 
            cost += dist 

            for i in range(len(points)):
                if i in visit:
                    continue
                
                manhattan = abs(points[index][0] - points[i][0]) + abs(points[index][1] - points[i][1])
                heapq.heappush(min_heap, (manhattan, i))  

        return cost
